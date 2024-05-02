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