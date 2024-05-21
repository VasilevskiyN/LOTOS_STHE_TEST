import requests

login = 1455
password = 19052013
# login = int(input('Введите login '))
# password = int(input('Введите password '))

URL_LOGIN = 'http://localhost:8000/check_login'
data = {'login': login, 'password': password}
check = requests.get(URL_LOGIN, params=data)
print(check)
result_text = check.json()['text']
result_data = check.json()['result']
print(result_text)
if result_data == True:
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

    hp_id = 1
    hp_uid = 1
    hp_reports_count = 1
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

    print("Запрос ушел")
    URL_DATA = 'http://localhost:8000/record_data'
    data2 = {
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
    finish = requests.post(URL_DATA, params=data2)
    print(finish.text)