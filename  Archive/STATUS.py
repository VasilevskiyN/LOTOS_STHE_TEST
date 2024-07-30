import requests
import time

UUID = str(input('Введите номер задачи '))
print(UUID)
lang = 'ru'
API_URL1 = 'http://192.168.1.145:8000/task_status'
data1 = {'task_id': UUID,  'lang': lang}
result1 = requests.post(API_URL1, params=data1)
print(result1.json())
prom = result1.json()
if prom['rez'] == 0:
    print(prom['error_info'])
if prom['rez'] == 1:
    print(result1)
    prom = result1.json()
    print(prom)
    task_status = prom['status']
    print(task_status)
    while "SUCCESS" not in task_status:
        result2 = requests.post(API_URL1, params=data1)
        prom1 = result2.json()
        print(prom1)
        task_status = prom1['status']
        print(task_status)
        time.sleep(10)
    if "SUCCESS" in task_status:
        if prom1['answer'] == 11:
            print(f'''
                Задача: \n
                Имя организации: {prom1['org'][0]}
                Номер задачи: {UUID} \n
                Исходные данные: \n
                Температура горячей воды на входе: {prom1['T1'][0]} °C
                Температура горячей воды на выходе: {prom1['T2'][0]} °C
                Расход горячей воды: {prom1['G'][0]} кг/ч
                Температура холодной воды на входе: {prom1['t1'][0]} °C
                Температура холодной воды на выходе: {prom1['t2'][0]} °C
                Расход холодной воды: {prom1['g'][0]} кг/ч \n
                Результаты расчета: \n
                {prom1['N'][0]} МВт
                ''')
        elif prom1['answer'] == 12:
            print(f'''
            Исходная дата: {prom1['data']} \n
            Результат: {prom1['heat_balance']}       
            ''')

