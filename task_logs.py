import requests

UUID = input("Введите uuid: ")
API_URL = 'http://192.168.1.145:8000/sthe/api/v2.0/task_logs'
api_key = "12345"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {"uuid": UUID}
result = requests.post(API_URL, json=data, headers=headers)
if result.status_code == 200:
    print(result.json()["task_logs"][0])
else:
    print(f"Ошибка: {result.status_code}, {result.text}")