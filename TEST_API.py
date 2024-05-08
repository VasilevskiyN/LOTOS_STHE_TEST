import requests
import time
import random

r = random.randint(0, 4)
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

API_URL='http://localhost:8000/dashboard'
data = {'login': login, 'number': number, 't1': t1, 't2': t2, 'T1': T1, 'T2': T2, 'g': g, 'G': G}
result = requests.post(API_URL,params = data)
print(f"Задача № {result.text} получена")
task_id = result.text
task_status = ""
prom = {}
while "SUCCESS" not in task_status:
    API_URL1 = f'http://localhost:8000/result_status?task_id={task_id}'
    result1 = requests.get(API_URL1)
    time.sleep(10)
    prom = result1.json()
    task_status = prom['status']
    print(task_status)
print(f''' Задача: \n 
        Имя организации: {prom['org']} \n
        Номер задачи: {result.text} \n
        Исходные данные: \n
        Температура горячей воды на входе: {prom['T1']} \n
        Температура горячей воды на выходе: {prom['T2']} \n
        Расход горячей воды: {prom['G']} \n
        Температура холодной воды на входе: {prom['t1']} \n
        Температура холодной воды на выходе: {prom['t2']} \n
        Расход холодной воды: {prom['g']} \n
        Результаты расчета: \n
        {prom['N']}
        ''')