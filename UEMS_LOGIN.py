import requests
import random
import string
from datetime import datetime
import sys

# DATA = {}
# PROCESS = 0
# TABL = 0
#
# def generate_random_text(length=10):
#     letters = string.ascii_letters + ' '
#     return ''.join(random.choice(letters) for i in range(length))
#
#
# def print_current_time():
#     now = datetime.now()
#     time_string = now.strftime("%H:%M:%S")
#     return time_string
#
#
# login = 1455
# password = 19052013
# # login = int(input('Введите login '))
# # password = int(input('Введите password '))
#
# URL_LOGIN = 'http://localhost:8000/check_login'
# data = {'login': login, 'password': password}
# check = requests.get(URL_LOGIN, params=data)
# result_text = check.json()['text']
# result_data = check.json()['result']
# if result_data == True:
#     print(f'''
#         Выберете рабочую таблицу:
#             1) Heat Project
#             2) Heat Balance
#             3) Heat Construction
#             ''')
#     TABL = int(input("Работаем с таблицей № "))
#
#     if TABL == 2 or TABL == 3:
#         id_project = int(input('Введите ID проекта '))
#         URL_CHECK = 'http://localhost:8000/check_project'
#         data_check = {'id_project':id_project}
#         check = requests.get(URL_CHECK, params=data_check)
#         if check.text != '1':
#             print("Проекта с таким id не существует")
#             sys.exit(0)
#
#     print(f'''
#     Возможные действия с таблицей:
#         1) Создать строку
#         2) Редактировать строку
#         3) Удалить строку
#         4) Выгрузить данные
#         ''')
#     PROCESS = int(input("Введите номер действия с проектом: "))
#     if PROCESS == 1 and TABL == 1:
#         print('Введите данные')
#         hp_uid = random.randint(1, 10)
#         hp_reports_count = random.randint(1, 15)
#         hp_array = generate_random_text(10)
#         hp_user_comment = generate_random_text(50)
#         hp_datetime = print_current_time()
#         hp_lastupd = generate_random_text(10)
#         hp_username = generate_random_text(5)
#         hp_usercompany = generate_random_text(10)
#         hp_jobid = random.randint(1, 10)
#         hp_hbid = random.randint(1, 10)
#         hp_hconstructionid = random.randint(1, 25)
#         hp_status = random.randint(1, 20)
#         # URL_DATA = 'http://localhost:8000/heat_project/create_project'
#         DATA = [hp_uid, hp_reports_count, hp_array, hp_user_comment, hp_datetime,
#             hp_lastupd, hp_username, hp_usercompany, hp_jobid, hp_hbid, hp_hconstructionid, hp_status]
#         # finish_create = requests.post(URL_DATA, params=DATA_CREATE)
#         # print(finish_create.text)
#
#     if PROCESS == 2 and TABL == 1:
#         hp_id = str(input('Введите id проекта для редактирования: '))
#         print("Выберите строки для изменения знаком +")
#         hp_uid_s = str(input('Значение uid '))
#         hp_reports_count_s = str(input('Значение reports_count '))
#         hp_array_s = str(input('Значение  array '))
#         hp_user_comment_s = str(input('Значение  user_comment '))
#         hp_datetime_s = str(input('Значение  datetime '))
#         hp_lastupd_s = str(input('Значение  lastupd '))
#         hp_username_s = str(input('Значение  username '))
#         hp_usercompany_s = str(input('Значение  usercompany '))
#         hp_jobid_s = str(input('Значение jobid '))
#         hp_hbid_s = str(input('Значение  hbid '))
#         hp_hconstructionid_s = str(input('Значение hconstructionid '))
#         hp_status_s = str(input('Значение  status '))
#         a = ['hp_uid', 'hp_reports_count', 'hp_array', 'hp_user_comment', 'hp_datetime', 'hp_lastupd', 'hp_username',
#              'hp_usercompany', 'hp_jobid', 'hp_hbid', 'hp_hconstructionid', 'hp_status']
#         b = [hp_uid_s, hp_reports_count_s, hp_array_s, hp_user_comment_s, hp_datetime_s, hp_lastupd_s, hp_username_s,
#              hp_usercompany_s, hp_jobid_s, hp_hbid_s, hp_hconstructionid_s, hp_status_s]
#         i = 0
#         print(b)
#         for i in range(len(b)):
#             if b[i] == '+':
#                 name = a[i]
#                 value = str(input(f'Введите {name} '))
#                 DATA = {'hp_id':hp_id,
#                                'name': name,
#                                'value': value
#                                }
#                 # URL_UPDATE = 'http://localhost:8000/heat_project/update_project'
#         #         finish_update = requests.post(URL_UPDATE, params=DATA_UPDATE)
#         # print(finish_update.text)
#
#     if PROCESS == 3 and TABL == 1:
#         ID = int(input('Введите id проекта для удаления: '))
#         # URL_DELETE = 'http://localhost:8000/heat_project/delete_project'
#         DATA = {'id':ID}
#         # finish_delete = requests.get(URL_DELETE, params=DATA_DELETE)
#         # print(finish_delete.text)
#
#     if PROCESS == 1 and TABL == 2:
#         print('Введите данные')
#         hb_type = random.randint(1, 10)
#         hb_hpid = id_project
#         hb_uid = random.randint(1, 15)
#         hb_array = generate_random_text(50)
#         hb_user_comment = generate_random_text(10)
#         hb_datetime = generate_random_text(10)
#         hb_lastup = print_current_time()
#         hb_username = generate_random_text(10)
#         hb_Q = random.randint(1, 10)
#         hb_LMTD = random.randint(1, 10)
#         hb_status = random.randint(1, 25)
#         hb_props_array_bytes = random.randint(1, 20)
#         # URL_DATA = 'http://localhost:8000/heat_balance/create_project'
#         DATA = [hb_type, hb_hpid, hb_uid, hb_array, hb_user_comment, hb_datetime, hb_lastup, hb_username, hb_Q,
#                 hb_LMTD, hb_status, hb_props_array_bytes]
#         # finish_create = requests.post(URL_DATA, params=DATA_CREATE)
#         # print(finish_create.text)
#
#     if PROCESS == 2 and TABL == 2:
#         hb_id = str(input('Введите id строки для редактирования: '))
#         hb_type = str(input('Значение type '))
#         hb_uid = str(input('Значение  uid '))
#         hb_array = str(input('Значение  array '))
#         hb_user_comment = str(input('Значение  user_comment '))
#         hb_datetime = str(input('Значение  datetime '))
#         hb_lastup = str(input('Значение  lastup '))
#         hb_username = str(input('Значение  username '))
#         hb_Q = str(input('Значение Q '))
#         hb_LMTD = str(input('Значение  LMTD '))
#         hb_status = str(input('Значение status '))
#         hb_props_array_bytes = str(input('Значение  props_array_bytes '))
#         # a = ['hb_type', 'hb_uid', 'hb_array', 'hb_user_comment', 'hb_datetime',
#         #     'hb_lastup', 'hb_username', 'hb_Q', 'hb_LMTD', 'hb_status', 'hb_props_array_bytes']
#         DATA = [hb_type, hb_uid, hb_array, hb_user_comment, hb_datetime,
#             hb_lastup, hb_username, hb_Q, hb_LMTD, hb_status, hb_props_array_bytes, hb_id]
#         # i = 0
#         # print(b)
#         # for i in range(len(b)):
#         #     if b[i] == '+':
#         #         name = a[i]
#         #         value = str(input(f'Введите {name} '))
#         #         DATA = {'hb_id':hb_id,
#         #                        'name': name,
#         #                        'value': value
#         #                        }
#                 # URL_UPDATE = 'http://localhost:8000/heat_balance/update_project'
#         #         finish_update = requests.post(URL_UPDATE, params=DATA_UPDATE)
#         # print(finish_update.text)
#
#     if PROCESS == 3 and TABL == 2:
#         ID = int(input('Введите id строки для удаления: '))
#         # URL_DELETE = 'http://localhost:8000/heat_balance/delete_project'
#         DATA = [ID]
#         # finish_delete = requests.get(URL_DELETE, params=DATA_DELETE)
#         # print(finish_delete.text)
#
#     if PROCESS == 4 and TABL == 2:
#         ID = int(input('Введите id строки для выгрузки '))
#         DATA = [ID]
#
#     if PROCESS == 1 and TABL == 3:
#         print('Введите данные')
#         hconstruction_hpid = id_project
#         hconstruction_name = generate_random_text(10)
#         hconstruction_uid = generate_random_text(10)
#         hconstruction_array = generate_random_text(10)
#         hconstruction_datetime = print_current_time()
#         hconstruction_username = generate_random_text(10)
#         hconstruction_status = random.randint(1, 25)
#         # URL_DATA = 'http://localhost:8000/heat_construction/create_project'
#         DATA = {
#             'hconstruction_hpid': hconstruction_hpid,
#             'hconstruction_name': hconstruction_name,
#             'hconstruction_uid': hconstruction_uid,
#             'hconstruction_array': hconstruction_array,
#             'hconstruction_datetime': hconstruction_datetime,
#             'hconstruction_username': hconstruction_username,
#             'hconstruction_status': hconstruction_status
#         }
#         # finish_create = requests.post(URL_DATA, params=DATA_CREATE)
#         # print(finish_create.text)
#
#     if PROCESS == 2 and TABL == 3:
#         hconstruction_id = str(input('Введите id строки для редактирования: '))
#         print("Выберите строки для изменения знаком +")
#         hconstruction_name_s = str(input('Значение name '))
#         hconstruction_uid_s = str(input('Значение  uid '))
#         hconstruction_array_s = str(input('Значение  array '))
#         hconstruction_datetime_s = str(input('Значение  user_comment '))
#         hconstruction_username_s = str(input('Значение  datetime '))
#         hconstruction_status_s = str(input('Значение  lastup '))
#         a = ['hconstruction_name', 'hconstruction_uid', 'hconstruction_array',
#              'hconstruction_datetime', 'hconstruction_username', 'hconstruction_status']
#         b = [hconstruction_name_s, hconstruction_uid_s, hconstruction_array_s,
#              hconstruction_datetime_s, hconstruction_username_s, hconstruction_status_s]
#         i = 0
#         print(b)
#         for i in range(len(b)):
#             if b[i] == '+':
#                 name = a[i]
#                 value = str(input(f'Введите {name} '))
#                 DATA = {'hconstruction_id':hconstruction_id,
#                                'name': name,
#                                'value': value
#                                }
#                 # URL_UPDATE = 'http://localhost:8000/heat_construction/update_project'
#         #         finish_update = requests.post(URL_UPDATE, params=DATA_UPDATE)
#         # print(finish_update.text)
#
#     if PROCESS == 3 and TABL == 3:
#         ID = int(input('Введите id строки для удаления: '))
#         # URL_DELETE = 'http://localhost:8000/heat_construction/delete_project'
#         DATA = {'id':ID}
#         # finish_delete = requests.get(URL_DELETE, params=DATA_DELETE)
#         # print(finish_delete.text)
#
# print('Новый подход')
# query = ''
# if PROCESS == 1:
#     insert_balace = (
#         'INSERT INTO UEMS_Heat_Balance SET hb_type = ?, hb_hpid = ?, hb_uid = ?, hb_array = ?, hb_user_comment = ?,'
#         'hb_datetime = ?, hb_lastup = ?, hb_username = ?, hb_Q = ?, hb_LMTD = ?, '
#         'hb_status = ?, hb_props_array_bytes =?')
#     query = insert_balace
#
# elif PROCESS == 2:
#     update_balanse = (
#         'UPDATE EMS_Heat_Balance SET hb_type = ?, hb_hpid = ?, hb_uid = ?, hb_array = ?, hb_user_comment = ?,'
#         'hb_datetime = ?, hb_lastup = ?, hb_username = ?, hb_Q = ?, hb_LMTD = ?, '
#         'hb_status = ?, hb_props_array_bytes =? WHERE hb_id = ?')
#     query = update_balanse
#
# elif PROCESS == 3:
#     delete_balance = ('DELETE FROM UEMS_Heat_Balance WHERE hb_id = ?')
#     query = delete_balance
#
# if PROCESS == 4:
#     select_balance = ('SELECT * FROM UEMS_Heat_Balance WHERE hb_id = ?')
#     query = select_balance

# parameters = DATA
URL_FULL = 'http://localhost:8000/heat_construction/query'
query =(
    "INSERT INTO UEMS_Heat_Balance (hb_type, hb_hpid, hb_uid, hb_array, "
    "hb_user_comment, hb_datetime, hb_lastup, hb_username, hb_Q, hb_LMTD, "
    "hb_status, hb_props_array_bytes) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
)
parameters = [7, 1, 5, 'ijDKXqNbOHGwTSwOQmFCGgV pxAMXVuDAdPMHnUBlSEouvtkWZ', 'wJljDczCBs', 'ASNZsemulP', '10:19:40',
              'YAybSnIvFJ', 4, 4, 12, 19]
data = {'query': query, 'parameters': parameters}
headers = {'Content-Type': 'application/json'}
response = requests.post(URL_FULL, headers=headers, json=data)
print(response.text)








