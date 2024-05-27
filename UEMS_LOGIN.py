import requests
import random

login = 1455
password = 19052013
# login = int(input('Введите login '))
# password = int(input('Введите password '))

URL_LOGIN = 'http://localhost:8000/check_login'
data = {'login': login, 'password': password}
check = requests.get(URL_LOGIN, params=data)
result_text = check.json()['text']
result_data = check.json()['result']
if result_data == True:
    print(f'''
    Возможные действия с проектом: 
        1) Создать проект 
        2) Редактировать проект 
        3) Удалить проект
        ''')
    PROCESS = int(input("Введите номер действия с проектом: "))
    if PROCESS == 1:
        print('Введите данные')
        # hp_id = int(input('Введите число id '))
        # hp_uid = int(input('Введите  число uid '))
        # hp_reports_count = int(input('Введите  число reports_count '))
        # hp_array = str(input('Введите текст array '))
        # hp_user_comment = str(input('Введите текст user_comment '))
        # hp_datetime = str(input('Введите текст datetime '))
        # hp_lastupd = str(input('Введите текст lastupd '))
        # hp_username = str(input('Введите текст username '))
        # hp_usercompany = str(input('Введите текст usercompany '))
        # hp_jobid = int(input('Введите число jobid '))
        # hp_hbid = int(input('Введите число hbid '))
        # hp_hconstructionid = int(input('Введите число hconstructionid '))
        # hp_status = int(input('Введите число status '))

        hp_id = random.randint(1, 1000)
        hp_uid = 12
        hp_reports_count = 12
        hp_array = 'a'
        hp_user_comment = 'a'
        hp_datetime = 'a'
        hp_lastupd = 'a'
        hp_username = 'a'
        hp_usercompany = 'a'
        hp_jobid = 1
        hp_hbid = 1
        hp_hconstructionid = 1
        hp_status = 1
        URL_DATA = 'http://localhost:8000/create_project'
        DATA_CREATE = {
            'hp_id': hp_id,
            'hp_uid': hp_uid,
            'hp_reports_count': hp_reports_count,
            'hp_array': hp_array,
            'hp_user_comment': hp_user_comment,
            'hp_datetime': hp_datetime,
            'hp_lastupd': hp_lastupd,
            'hp_username': hp_username,
            'hp_usercompany': hp_usercompany,
            'hp_jobid': hp_jobid,
            'hp_hbid': hp_hbid,
            'hp_hconstructionid': hp_hconstructionid,
            'hp_status': hp_status
        }
        finish_create = requests.post(URL_DATA, params=DATA_CREATE)
        print(finish_create.text)

    if PROCESS == 2:
        hp_id = str(input('Введите id проекта для редактирования: '))
        print("Выберите строки для изменения знаком +")
        hp_uid_s = str(input('Значение uid '))
        hp_reports_count_s = str(input('Значение reports_count '))
        hp_array_s = str(input('Значение  array '))
        hp_user_comment_s = str(input('Значение  user_comment '))
        hp_datetime_s = str(input('Значение  datetime '))
        hp_lastupd_s = str(input('Значение  lastupd '))
        hp_username_s = str(input('Значение  username '))
        hp_usercompany_s = str(input('Значение  usercompany '))
        hp_jobid_s = str(input('Значение jobid '))
        hp_hbid_s = str(input('Значение  hbid '))
        hp_hconstructionid_s = str(input('Значение hconstructionid '))
        hp_status_s = str(input('Значение  status '))
        a = ['hp_uid', 'hp_reports_count', 'hp_array', 'hp_user_comment', 'hp_datetime', 'hp_lastupd', 'hp_username',
             'hp_usercompany', 'hp_jobid', 'hp_hbid', 'hp_hconstructionid', 'hp_status']
        b = [hp_uid_s, hp_reports_count_s, hp_array_s, hp_user_comment_s, hp_datetime_s, hp_lastupd_s, hp_username_s,
             hp_usercompany_s, hp_jobid_s, hp_hbid_s, hp_hconstructionid_s, hp_status_s]
        i = 0
        print(b)
        for i in range(len(b)):
            if b[i] == '+':
                name = a[i]
                value = str(input(f'Введите {name} '))
                DATA_UPDATE = {'hp_id':hp_id,
                               'name': name,
                               'value': value
                               }
                URL_UPDATE = 'http://localhost:8000/update_project'
                finish_update = requests.post(URL_UPDATE, params=DATA_UPDATE)
        print(finish_update.text)

    if PROCESS == 3:
        ID = int(input('Введите id проекта для удаления: '))
        URL_DELETE = 'http://localhost:8000/delete_project'
        DATA_DELETE = {'id':ID}
        finish_delete = requests.get(URL_DELETE, params=DATA_DELETE)
        print(finish_delete.text)

