import re
import ast
import datetime
import sqlite3
from sqlite3 import OperationalError

def create_db_if_absent(cursor):
    try:
        cursor.execute("""CREATE TABLE citizens
                          (import_id integer, citizen_id integer, town text,
                          street text, building text, apartment integer,
                          name text, birth_date text, gender text,
                          relatives text)
                       """)
    except OperationalError:
        pass

def get_last_import_id(cursor):
    cursor.execute("SELECT MAX(import_id) FROM citizens")
    import_id = cursor.fetchall()[0][0]
    if import_id is None:
        return -1
    else:
        return import_id

def exists(import_id, citizen_id, cursor):    
    cursor.execute("SELECT * FROM citizens WHERE (citizen_id = "+str(citizen_id)+") AND (import_id = "+str(import_id)+")")
    result = cursor.fetchall()
    if result == []:
        return False
    else:
        return True
    
def info(import_id, citizen_id, cursor):
    
    cursor.execute("SELECT * FROM citizens WHERE (citizen_id = "+str(citizen_id)+") AND (import_id = "+str(import_id)+")")
    result = cursor.fetchall()[0]
    data = {
        "data" : {
            "citizen_id": result[1],
            "town": result[2],
            "street": result[3],
            "building": result[4],
            "apartment": result[5],
            "name": result[6],
            "birth_date": result[7],
            "gender": result[8],
            "relatives": ast.literal_eval(result[9])
        }
    }
    return data

def global_info(import_id, cursor):
    
    cursor.execute("SELECT * FROM citizens WHERE import_id = "+str(import_id))
    result = cursor.fetchall()
    data = {
        "data" : [{
            "citizen_id": i[1],
            "town": i[2],
            "street": i[3],
            "building": i[4],
            "apartment": i[5],
            "name": i[6],
            "birth_date": i[7],
            "gender": i[8],
            "relatives": ast.literal_eval(i[9])
        } for i in result]
    }
    return data

def put_in_db(obj, IMPORT_ID, cursor, conn):
    data = []
    for i in obj['citizens']:
        data.append((str(IMPORT_ID), str(i['citizen_id']), i['town'], 
                    i['street'], i['building'], str(i['apartment']),
                    i['name'], i['birth_date'], i['gender'],
                    str(i['relatives'])))
    cursor.executemany("INSERT INTO citizens VALUES (?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    
def put_change_in_db(obj, import_id, citizen_id, cursor, conn):
    data = info(import_id, citizen_id, cursor)['data']
    prev_relatives = None
    for key in obj.keys():
        if key == 'relatives':
            prev_relatives = data[key] 
        data[key] = obj[key]
    cursor.execute("UPDATE citizens \
                    SET town = \'"+data['town']+"\', \
                        street = \'"+data['street']+"\', \
                        building = \'"+data['building']+"\', \
                        apartment = \'"+str(data['apartment'])+"\', \
                        name = \'"+data['name']+"\', \
                        birth_date = \'"+data['birth_date']+"\', \
                        gender = \'"+data['gender']+"\', \
                        relatives = \'"+str(data['relatives'])+"\' \
                    WHERE (import_id = "+str(import_id)+") AND \
                          (citizen_id = "+str(citizen_id)+")"
                   )
    conn.commit()
    
    if prev_relatives is not None:
        relatives_to_delete = list(set(prev_relatives) - set(data['relatives']))
        new_relatives = list(set(data['relatives']) - set(prev_relatives))
        
        if len(relatives_to_delete) == 1:
            cursor.execute("SELECT * FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN ("+str(relatives_to_delete[0])+"))")
            relatives = cursor.fetchall()
            cursor.execute("DELETE FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN ("+str(relatives_to_delete[0])+"))")
            conn.commit()
            
        if len(relatives_to_delete) > 1:
            cursor.execute("SELECT * FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN "+str(tuple(relatives_to_delete))+")")
            relatives = cursor.fetchall()
            cursor.execute("DELETE FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN "+str(tuple(relatives_to_delete))+")")
            conn.commit()
            
        for i in range(len(relatives_to_delete)):
            l = ast.literal_eval(relatives[i][9])
            del l[l.index(citizen_id)]
            relatives[i] = list(relatives[i])
            relatives[i][-1] = str(l)
            relatives[i] = tuple(relatives[i])
            
        if len(relatives_to_delete) > 0:
            cursor.executemany("INSERT INTO citizens VALUES (?,?,?,?,?,?,?,?,?,?)", relatives)
            conn.commit()
            
        if len(new_relatives) == 1:
            cursor.execute("SELECT * FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN ("+str(new_relatives[0])+"))")
            relatives = cursor.fetchall()
            cursor.execute("DELETE FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN ("+str(new_relatives[0])+"))")
            conn.commit()
            
        if len(new_relatives) > 1:
            cursor.execute("SELECT * FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN "+str(tuple(new_relatives))+")")
            relatives = cursor.fetchall()
            cursor.execute("DELETE FROM citizens WHERE (import_id = "+str(import_id)+") AND\
                                                         (citizen_id IN "+str(tuple(new_relatives))+")")
            conn.commit()
            
        for i in range(len(new_relatives)):
            l = ast.literal_eval(relatives[i][9])
            l.append(citizen_id)
            relatives[i] = list(relatives[i])
            relatives[i][-1] = str(l)
            relatives[i] = tuple(relatives[i])
            
        if len(new_relatives) > 0:
            cursor.executemany("INSERT INTO citizens VALUES (?,?,?,?,?,?,?,?,?,?)", relatives)
            conn.commit()
        
def check_valid(obj):
    known_ids = set()
    relatives = dict()
    pattern = re.compile('.*[\dA-Za-zа-яА-Я]')
    needed_keys = {'apartment', 'birth_date', 'building', 'citizen_id',
                   'gender', 'name', 'relatives', 'street', 'town'} 
    try:
        if list(obj.keys()) != ['citizens']:
            return False
        for i in obj['citizens']:
            if i.keys() == needed_keys and \
                    type(i['citizen_id']) == int and \
                    i['citizen_id'] >= 0 and \
                    i['citizen_id'] not in known_ids and \
                    type(i['town']) == str and \
                    pattern.match(i['town']) and \
                    len(i['town']) <= 256 and \
                    type(i['street']) == str and \
                    pattern.match(i['street']) and \
                    len(i['street']) <= 256 and \
                    type(i['building']) == str and \
                    pattern.match(i['building']) and \
                    len(i['building']) <= 256 and \
                    type(i['apartment']) == int and \
                    i['apartment'] >= 0 and \
                    type(i['name']) == str and \
                    len(i['name']) != 0 and \
                    len(i['name']) <= 256 and \
                    i['gender'] in ['male', 'female'] and \
                    type(i['relatives']) == list and \
                    all(isinstance(j, int) for j in i['relatives']) and \
                    datetime.datetime.strptime(i['birth_date'], "%d.%m.%Y") < datetime.datetime.now():
                known_ids.add(i['citizen_id'])
                if len(i['relatives']) != 0:
                    relatives[i['citizen_id']] = set(i['relatives']) # 
                    if len(i['relatives']) != len(relatives[i['citizen_id']]):
                        return False
            else:
                return False
        try:
            for k in relatives.keys():
                for j in relatives[k]:
                    relatives[j].remove(k)
            return True
        except:
            return False
    except:
        return False        
    
def check_valid_change(i, import_id, citizen_id, cursor):

    if not exists(import_id, citizen_id, cursor):
        return False
    
    pattern = re.compile('.*[\dA-Za-zа-яА-Я]')
    needed_keys = {'apartment', 'birth_date', 'building',
                   'gender', 'name', 'relatives', 'street', 'town'} 
    try:
        if set(i.keys()).issubset(needed_keys) and len(i.keys()) != 0:
            if 'town' in i.keys():
                if not (type(i['town']) == str and \
                   pattern.match(i['town']) and \
                   len(i['town']) <= 256):
                    return False
            if 'street' in i.keys():
                if not (type(i['street']) == str and \
                   pattern.match(i['street']) and \
                   len(i['street']) <= 256):
                    return False
            if 'building' in i.keys():
                if not (type(i['building']) == str and \
                   pattern.match(i['building']) and \
                   len(i['building']) <= 256):
                    return False
            if 'apartment' in i.keys():
                if not (type(i['apartment']) == int and \
                   i['apartment'] >= 0):
                    return False
            if 'name' in i.keys():
                if not (type(i['name']) == str and \
                   len(i['name']) != 0 and \
                   len(i['name']) <= 256):
                    return False
            if 'gender' in i.keys():
                if not i['gender'] in ['male', 'female']:
                    return False
            if 'relatives' in i.keys():
                if not (type(i['relatives']) == list and \
                   all(isinstance(j, int) for j in i['relatives']) and \
                   len(i['relatives']) == len(set(i['relatives'])) and \
                   citizen_id not in i['relatives']):
                    return False
                if len(i['relatives']) == 1:
                    cursor.execute("SELECT COUNT(1) FROM citizens WHERE (import_id = "+str(import_id)+") AND (citizen_id IN ("+str(i['relatives'][0])+"))")
                    result = cursor.fetchall()[0][0]
                    if result != len(i['relatives']):
                        return False
                if len(i['relatives']) > 1:
                    cursor.execute("SELECT COUNT(1) FROM citizens WHERE (import_id = "+str(import_id)+") AND (citizen_id IN "+str(tuple(i['relatives']))+")")
                    result = cursor.fetchall()[0][0]
                    if result != len(i['relatives']):
                        return False
            if 'birth_date' in i.keys():
                if not (datetime.datetime.strptime(i['birth_date'], "%d.%m.%Y") < datetime.datetime.now()):
                    return False
            return True
        else:
            return False
    except:
        return False        
    
