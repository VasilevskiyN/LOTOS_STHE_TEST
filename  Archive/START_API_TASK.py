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
password = b[str(login)]
T1 = int(random.randint(70, 100))
T2 = int(random.randint(55, 65))
t1 = int(random.randint(5, 15))
t2 = int(random.randint(20, 35))
g = int(random.randint(10, 50))
# G = int(random.randint(10, 50))
G = None

#login = int(input('Введите login '))
#number = int(input('Введите number '))
#T1 = int(input('Введите температуру на входе горячего потока '))
#T2 = int(input('Введите температуру на выходе горячего потока '))
#t1 = int(input('Введите температуру на входе холодного потока '))
#t2 = int(input('Введите температуру на выходе холодного потока '))
#g = int(input('Введите расход холодной среды '))
#G = int(input('Введите расход горячей среды '))

API_URL='http://192.168.1.145:8000/authorization'
# API_URL='http://localhost:8000/dashboard'
data = {'login': login, 'password': password}
authorization_res = requests.get(API_URL, params=data)
authorization_result = authorization_res.json()
print(authorization_result['message'])
name = authorization_result['organization']
if authorization_result['user'] is True:
    print(f"Возможные варианты:"
          "1) Посчитать тепловой баланс"
          "2) Выполнить теплотехнический расчет")
    action = int(input('Введите номер действия: '))
if action == 1:
    API_URL = 'http://192.168.1.145:8000/heat_balance'
    data = {'login': login, 'password': password, 'T1': T1, 'T2': T2, 'G': G, 't1': t1, 't2': t2, 'g': g}
    result = requests.post(API_URL, params=data)
    print(result.text)
elif action == 2:
    API_URL = 'http://192.168.1.145:8000/thermal_power'
    data = {'login': login, 'password': password, 'T1': T1, 'T2':T2, 'G':G, 't1':t1, 't2':t2, 'g':g }
    result = requests.post(API_URL,params = data)
    print(f'{result.text}')


