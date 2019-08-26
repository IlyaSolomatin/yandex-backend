from flask import Flask
from flask import request
from flask import abort
import json
from utils import *
import sqlite3 

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

create_db_if_absent(cursor)

@app.route('/imports', methods=['POST'])
def get_data():
    
    obj = request.get_json(force=True)
    if check_valid(obj):
        import_id = get_last_import_id(cursor) + 1
        put_in_db(obj, import_id, cursor, conn)
        return json.loads('{\"data\":{\"import_id\":' + str(import_id) + '}}'), 201
    else:
        abort(400) 
        
@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def change_data(import_id, citizen_id):
    
    obj = request.get_json(force=True)
    if check_valid_change(obj, import_id, citizen_id, cursor):
        put_change_in_db(obj, import_id, citizen_id, cursor, conn)
        return info(import_id, citizen_id, cursor), 200
    else:
        abort(400) 
        
@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def send_data(import_id):
    data = global_info(import_id, cursor)
    if data["data"] == []:
        abort(404)
    return data, 200
    
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
