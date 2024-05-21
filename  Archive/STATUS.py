import requests
import time

UUID = str(input('Введите номер задачи '))
print(UUID)
API_URL1 = f'http://localhost:8000/task_status?task_id={UUID}'
result1 = requests.get(API_URL1)
print(result1)
prom = result1.json()
print(prom)
task_status = prom['status']
print(task_status)
while "SUCCESS" not in task_status:
    result1 = requests.get(API_URL1)
    prom = result1.json()
    task_status = prom['status']
    print(task_status)
    time.sleep(10)
print(f'''
Задача: \n
Имя организации: {prom['org'][0]} 
Номер задачи: {UUID} \n
Исходные данные: \n
Температура горячей воды на входе: {prom['T1'][0]} °C
Температура горячей воды на выходе: {prom['T2'][0]} °C
Расход горячей воды: {prom['G'][0]} кг/ч
Температура холодной воды на входе: {prom['t1'][0]} °C
Температура холодной воды на выходе: {prom['t2'][0]} °C
Расход холодной воды: {prom['g'][0]} кг/ч \n 
Результаты расчета: \n
{prom['N'][0]} МВт
''')