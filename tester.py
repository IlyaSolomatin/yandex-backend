import requests
import json

print("Тест обработчика 1: POST /imports")
#Обращение к несуществующей ссылке
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/importssss'
r = requests.post(url, data=json.dumps(payload))
print("Обращение к несуществующей ссылке:", r.status_code == 404)

#Отправка поломаного json объекта
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload)[:-2])
print("Отправка поломаного json объекта:", r.status_code == 400)

#Наличие не описанных полей - 1
payload = {"noncitizens": [],
           "citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("Наличие не описанных полей - 1:", r.status_code == 400)

#Наличие не описанных полей - 2
payload = {"citizens":[
{"citizen_id": 1,
 "passport": "Yes",
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("Наличие не описанных полей - 2:", r.status_code == 400)

#null значения в поле
payload = {"citizens":[
{"citizen_id": 1,
"town": None,
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("null значения в поле:", r.status_code == 400)

#citizen_id не уникален в выгрузке
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []},
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("citizen_id не уникален в выгрузке:", r.status_code == 400)

#citizen_id не целое число
payload = {"citizens":[
{"citizen_id": 1.5,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("citizen_id не целое число:", r.status_code == 400)

#citizen_id не неотрицательное целое число
payload = {"citizens":[
{"citizen_id": -2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("citizen_id не неотрицательное целое число:", r.status_code == 400)

#citizen_id не число
payload = {"citizens":[
{"citizen_id": "Мда",
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("citizen_id не число:", r.status_code == 400)

#citizen_id отсутствует
payload = {"citizens":[
{"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("citizen_id отсутствует:", r.status_code == 400)

#town не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": 2,
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("town не строка:", r.status_code == 400)

#town отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("town отсутствует:", r.status_code == 400)

#town пустая строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("town пустая строка:", r.status_code == 400)

#town более 256 символов
payload = {"citizens":[
{"citizen_id": 1,
"town": "Мо"*129,
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("town более 256 символов:", r.status_code == 400)

#town не содержит ни одной буквы и цифры
payload = {"citizens":[
{"citizen_id": 1,
"town": "@$!@#!@#",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("town не содержит ни одной буквы и цифры:", r.status_code == 400)

#street не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": 2,
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("street не строка:", r.status_code == 400)

#street отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("street отсутствует:", r.status_code == 400)

#street пустая строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("street пустая строка:", r.status_code == 400)

#street более 256 символов
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "МО"*129,
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("street более 256 символов:", r.status_code == 400)

#street не содержит ни одной буквы и цифры
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "%!№!",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("street не содержит ни одной буквы и цифры:", r.status_code == 400)

#building не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": 2,
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("building не строка:", r.status_code == 400)

#building отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("building отсутствует:", r.status_code == 400)

#building пустая строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("building пустая строка:", r.status_code == 400)

#building более 256 символов
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "sad"*129,
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("building более 256 символов:", r.status_code == 400)

#building не содержит ни одной буквы и цифры
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "!@#!@",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("building более 256 символов:", r.status_code == 400)

#apartment отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("apartment отсутствует:", r.status_code == 400)

#apartment не число
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": "da",
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("apartment не число:", r.status_code == 400)

#apartment не неотрицательное число
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": -5,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("apartment не число:", r.status_code == 400)

#apartment не целое число
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 1.5,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("apartment не число:", r.status_code == 400)

#name отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("name отсутствует:", r.status_code == 400)

#name не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": 50,
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("name не строка:", r.status_code == 400)

#name пустая строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("name пустая строка:", r.status_code == 400)

#name больше 256 символов
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "DF"*129,
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("name пустая строка:", r.status_code == 400)

#birth date отсутсвует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("birth date отсутсвует:", r.status_code == 400)

#birth date не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": 43,
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("birth date не строка:", r.status_code == 400)

#birth date другого формата
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "1993.12.01",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("birth date другого формата:", r.status_code == 400)

#birth date не существующая дата
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "66.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("birth date не существующая дата:", r.status_code == 400)

#birth date больше текущей даты
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "01.12.3019",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("birth date больше текущей даты:", r.status_code == 400)

#gender отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("gender отсутствует:", r.status_code == 400)

#gender не строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": 23,
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("gender не строка:", r.status_code == 400)

#gender пустая строка
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("gender не строка:", r.status_code == 400)

#gender 'memale'
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "memale",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("gender не male или female:", r.status_code == 400)

#relatives отсутствует
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male"}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives отсутствует:", r.status_code == 400)

#relatives не список - 1
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": dict()}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives не список - 2:", r.status_code == 400)

#relatives не список - 2
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": 25}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives не список - 3:", r.status_code == 400)

#relatives содержит не только целые числа
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2, "Hey"]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives содержит не только целые числа:", r.status_code == 400)

#relatives содержит сам citizen_id
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1, 2]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives содержит сам citizen_id:", r.status_code == 400)

#relatives содержит повторения
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2, 2]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives содержит повторения:", r.status_code == 400)

#relatives содержит citizen_id не из этой выборки
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2, 3]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives содержит citizen_id не из этой выборки:", r.status_code == 400)

#relatives не двухсторонние
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": []}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
print("relatives не двухсторонние:", r.status_code == 400)

#валидный запрос
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2]},
{"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]}]}
ans = {"data": {"import_id": 0}}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
ans = json.loads(r.text)
if list(ans.keys()) == ['data'] and list(ans['data'].keys()) == ['import_id'] and \
   type(ans['data']['import_id']) == int and r.status_code == 201:
    print("валидный запрос:", True)
else:
    print("валидный запрос:", False)
    
print(" ")
print("Тест обработчика 2: PATCH /imports/$import_id/citizens/$citizen_id")
#Пустой запрос
payload = {}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("Пустой запрос:", r.status_code == 400)

#Есть значение null
payload = {"name": "Вася", "gender": None}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("Есть значение null:", r.status_code == 400)

#Указано неописанное поле
payload = {"name": "Вася", "gender": "female", "age": 30}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("Указано неописанное поле:", r.status_code == 400)

#Указано поле citizen_id
payload = {"name": "Вася", "gender": "female", "citizen_id": 1}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("Указано поле citizen_id:", r.status_code == 400)

#Обращение к несуществующему import_id
payload = {"name": "Вася", "gender": "female"}
url = 'http://0.0.0.0:8080/imports/25000/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("Обращение к несуществующему import_id:", r.status_code == 400)

#Обращение к несуществующему citizen_id
payload = {"name": "Вася", "gender": "female"}
url = 'http://0.0.0.0:8080/imports/0/citizens/38000'
r = requests.patch(url, data=json.dumps(payload))
print("Обращение к несуществующему citizen_id:", r.status_code == 400)

#Отправка поломаного json объекта
payload = {"name": "Вася", "gender": "female"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload)[:-2])
print("Отправка поломаного json объекта:", r.status_code == 400)

#town не строка
payload = {"name": "Вася", "town": 2}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("town не строка:", r.status_code == 400)

#town пустая строка
payload = {"name": "Вася", "town": ""}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("town пустая строка:", r.status_code == 400)

#town более 256 символов
payload = {"name": "Вася", "town": "WE"*129}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("town более 256 символов:", r.status_code == 400)

#town не содержит ни одной буквы и цифры
payload = {"name": "Вася", "town": "@!#"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("town не содержит ни одной буквы и цифры:", r.status_code == 400)

#street не строка
payload = {"name": "Вася", "street": dict()}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("street не строка:", r.status_code == 400)

#street пустая строка
payload = {"name": "Вася", "street": ""}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("street пустая строка:", r.status_code == 400)

#street более 256 символов
payload = {"name": "Вася", "street": "RE"*129}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("street более 256 символов:", r.status_code == 400)

#street не содержит ни одной буквы и цифры
payload = {"name": "Вася", "street": "!$@$!@"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("street не содержит ни одной буквы и цифры:", r.status_code == 400)

#building не строка
payload = {"name": "Вася", "building": 100}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("building не строка:", r.status_code == 400)

#building пустая строка
payload = {"name": "Вася", "building": ""}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("building пустая строка:", r.status_code == 400)

#building более 256 символов
payload = {"name": "Вася", "building": "kd"*129}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("building более 256 символов:", r.status_code == 400)

#building не содержит ни одной буквы и цифры
payload = {"name": "Вася", "building": "!@$!@$!"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("building не содержит ни одной буквы и цифры:", r.status_code == 400)

#apartment не число
payload = {"name": "Вася", "apartment": "Hey"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("apartment не число:", r.status_code == 400)

#apartment не неотрицательное число
payload = {"name": "Вася", "apartment": -5}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("apartment не неотрицательное число:", r.status_code == 400)

#apartment не целое число
payload = {"name": "Вася", "apartment": 1.5}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("apartment не целое число:", r.status_code == 400)

#name не строка
payload = {"name": "Вася", "name": 1.5}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("name не строка:", r.status_code == 400)

#name пустая строка
payload = {"name": "Вася", "name": ""}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("name пустая строка:", r.status_code == 400)

#name больше 256 символов
payload = {"name": "Вася", "name": "ву"*129}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("name больше 256 символов:", r.status_code == 400)

#birth date не строка
payload = {"name": "Вася", "birth_date": 10}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("birth date не строка:", r.status_code == 400)

#birth date другого формата
payload = {"name": "Вася", "birth_date": "1992.10.10"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("birth date другого формата:", r.status_code == 400)

#birth date не существующая дата
payload = {"name": "Вася", "birth_date": "10.13.1992"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("birth date не существующая дата:", r.status_code == 400)

#birth date больше текущей даты
payload = {"name": "Вася", "birth_date": "10.13.3992"}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("birth date больше текущей даты:", r.status_code == 400)

#gender не строка
payload = {"name": "Вася", "gender": 2}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("gender не строка:", r.status_code == 400)

#gender пустая строка
payload = {"name": "Вася", "gender": ""}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("gender пустая строка:", r.status_code == 400)

#gender 'memale'
payload = {"name": "Вася", "gender": 'memale'}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("gender не male или female:", r.status_code == 400)

#relatives не список - 1
payload = {"name": "Вася", "relatives": dict()}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives не список - 1:", r.status_code == 400)

#relatives не список - 2
payload = {"name": "Вася", "relatives": 2}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives не список - 2:", r.status_code == 400)

#relatives содержит не только целые числа
payload = {"name": "Вася", "relatives": [2, "Hey"]}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives содержит не только целые числа:", r.status_code == 400)

#relatives содержит сам citizen_id
payload = {"name": "Вася", "relatives": [1, 2]}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives содержит сам citizen_id:", r.status_code == 400)

#relatives содержит повторения
payload = {"name": "Вася", "relatives": [1, 2, 2]}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives содержит повторения:", r.status_code == 400)

#relatives содержит citizen_id не из этой выборки
payload = {"name": "Вася", "relatives": [15]}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
print("relatives содержит citizen_id не из этой выборки:", r.status_code == 400)

#валидный запроc
payload = {"name": "Вася", "gender": "male", "birth_date": "19.10.1992",
          "relatives": [2], "town": "Msk", "street": "H", 
          "building": "22", "apartment": 7}
url = 'http://0.0.0.0:8080/imports/0/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
ans = {'data': {'apartment': 7,
  'birth_date': '19.10.1992',
  'building': '22',
  'citizen_id': 1,
  'gender': 'male',
  'name': 'Вася',
  'relatives': [2],
  'street': 'H',
  'town': 'Msk'}}
print("валидный запроc:", json.loads(r.text) == ans and r.status_code == 200)

print(" ")
print("Тест обработчика 3: GET /imports/$import_id/citizens")
#Обращение к несуществующему import_id
url = 'http://0.0.0.0:8080/imports/300000/citizens'
r = requests.get(url)
print("Обращение к несуществующему import_id:", r.status_code == 404)

#Проверка только что закинутых данных
payload = {"citizens":[
{"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2]},
{"citizen_id": 2,
"town": "Спб",
"street": "Невский",
"building": "23",
"apartment": 6,
"name": "Вася",
"birth_date": "15.10.1986",
"gender": "male",
"relatives": [1, 3]},
{"citizen_id": 3,
"town": "Самара",
"street": "Пушкина",
"building": "40",
"apartment": 12,
"name": "Петя",
"birth_date": "22.12.1986",
"gender": "female",
"relatives": [2]}]}
url = 'http://0.0.0.0:8080/imports'
r = requests.post(url, data=json.dumps(payload))
import_id = json.loads(r.text)['data']['import_id']
url = 'http://0.0.0.0:8080/imports/'+str(import_id)+'/citizens'
r = requests.get(url)
payload['data'] = payload['citizens']
del payload['citizens']
print("Проверка только что закинутых данных:", json.loads(r.text) == payload)

#Проверка, что все поля человека изменились после патча + изменение родственников
payload = {"name": "Коля", "gender": "female", "birth_date": "19.10.1992",
          "relatives": [3], "town": "Msk", "street": "H", 
          "building": "22", "apartment": 27}
url = 'http://0.0.0.0:8080/imports/'+str(import_id)+'/citizens/1'
r = requests.patch(url, data=json.dumps(payload))
url = 'http://0.0.0.0:8080/imports/'+str(import_id)+'/citizens'
r = requests.get(url)
data = {"data":[
{"citizen_id": 1,
"town": "Msk",
"street": "H",
"building": "22",
"apartment": 27,
"name": "Коля",
"birth_date": "19.10.1992",
"gender": "female",
"relatives": [3]},
{"citizen_id": 2,
"town": "Спб",
"street": "Невский",
"building": "23",
"apartment": 6,
"name": "Вася",
"birth_date": "15.10.1986",
"gender": "male",
"relatives": [3]},
{"citizen_id": 3,
"town": "Самара",
"street": "Пушкина",
"building": "40",
"apartment": 12,
"name": "Петя",
"birth_date": "22.12.1986",
"gender": "female",
"relatives": [2,1]}]}
print("Проверка, что все поля человека изменились после патча + проверка изменений в родственниках:", data == json.loads(r.text))