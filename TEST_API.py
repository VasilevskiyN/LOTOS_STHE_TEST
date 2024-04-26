import requests
import time
import random

r= random.randint(0, 4)
a = [1455, 1877, 1355, 9548, 6432]
b = {
    '1455': 19052013,
    '1877': 28791562,
    '1355': 59843251,
    '9548': 91245684,
    '6432': 72648953
}
login = a[r]
number = b[str(login)]
T1 = random.randint(70, 100)
T2 = random.randint(55, 65)
t1 = random.randint(5, 15)
t2 = random.randint(20, 35)
g = random.randint(10, 50)
G = random.randint(10, 50)
#login = int(input('Введите login '))
#number = int(input('Введите number '))
#T1 = int(input('Введите температуру на входе горячего потока '))
#T2 = int(input('Введите температуру на выходе горячего потока '))
#t1 = int(input('Введите температуру на входе холодного потока '))
#t2 = int(input('Введите температуру на выходе холодного потока '))
#g = int(input('Введите расход холодной среды '))
#G = int(input('Введите расход горячей среды '))

API_URL='http://localhost:8000/license'
data1 = {'login' : login, 'number' : number}
result1 = requests.post(API_URL,params = data1)
print(result1, result1.text)

API_URL='http://localhost:8000/initial_data'
data =  {'t1':t1,'t2':t2,'T1':T1, 'T2':T2, 'g':g, 'G':G}
result = requests.post(API_URL,params = data)
print(result, result.text)

API_URL='http://localhost:8000/TEMA'
result2 = requests.get(API_URL)
print(result2, result2.text)

API_URL='http://localhost:8000/dashboard'
result3 = requests.get(API_URL)
task_id = result3.json()['task_id']
print(result3.json())

task_status = ''
while "SUCCESS" not in task_status:
    API_URL = f'http://localhost:8000/get_status?task_id={task_id}'
    result4 = requests.get(API_URL)
    time.sleep(5)
    task_status = result4.text
    print(task_status)
print(f"Задача № {task_id} выполнена")
