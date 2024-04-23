import requests
import time
# Ниже указал действующие login // number для запуска кода
# 1455 //19052013
# 1877 // 28791562
# 1355 // 59843251
# 9548 // 91245684
# 6432 // 72648953
login = int(input('Введите login '))
number = int(input('Введите number '))
T1 = int(input('Введите температуру на входе горячего потока '))
T2 = int(input('Введите температуру на выходе горячего потока '))
t1 = int(input('Введите температуру на входе холодного потока '))
t2 = int(input('Введите температуру на выходе холодного потока '))
g = int(input('Введите расход холодной среды '))
G = int(input('Введите расход горячей среды '))

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