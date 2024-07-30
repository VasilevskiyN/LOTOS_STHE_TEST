import requests

UUID = str(input("Введите индентификатор задачи "))
lang = 'ru'
API_URL1 = 'http://192.168.1.145:8000/sthe/api/v2.0/task_result'
data1 = {'uuid': UUID,  'lang': lang}

api_key = "12345"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

with requests.post(API_URL1, params=data1,  headers=headers) as response:
    print(response.text)