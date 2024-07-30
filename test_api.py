import requests
import data
import time
import json

url = "http://192.168.1.145:8000/sthe/api/v2.0/task_create"
api_key = "12345"
payload = {
    "method": "heat_balance",
    "data": {"UserInput": data.UserInput, "UserAnswers": data.UserAnswers},
}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
response = response.json()
print(response)
task_result = None
while task_result is None:
    time.sleep(5)
    print("Ожидание ...")
    UUID = response["uuid"]
    API_URL = 'http://192.168.1.145:8000/sthe/api/v2.0/task_status'
    full_url = f"{API_URL}/{UUID}"
    result = requests.get(full_url, headers=headers)
    if result.status_code == 200:
        try:
            response_data = result.json()
            print(f"Идентификатор задачи: {response_data['task_id']}")
            print(f"Статус задачи: {response_data['status']}")
            if response_data['status'] == "Success":
                lang = 'ru'
                API_URL1 = 'http://192.168.1.145:8000/sthe/api/v2.0/task_result'
                data1 = {'uuid': UUID, 'lang': lang}
                with requests.post(API_URL1, params=data1, headers=headers) as response:
                    task_result = json.loads(response.text)
        except requests.exceptions.JSONDecodeError:
            print("Не удалось распарсить ответ как JSON. Вывод текста ответа:")
            print(result.text)
    else:
        print(f"Ошибка при выполнении запроса. Код статуса: {result.status_code}")
        print(f"Текст ответа: {result.text}")

print(task_result)
