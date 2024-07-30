import requests

UUID = input('Введите номер задачи: ')
API_URL = 'http://192.168.1.145:8000/sthe/api/v2.0/task_status'

api_key = "12345"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

full_url = f"{API_URL}/{UUID}"

result = requests.get(full_url, headers=headers)

if result.status_code == 200:

    try:
        response_data = result.json()
        print(f"Идентификатор задачи: {response_data['task_id']}")
        print(f"Статус задачи: {response_data['status']}")
    except requests.exceptions.JSONDecodeError:
        print("Не удалось расcпаросить ответ как JSON. Вывод текста ответа:")
        print(result.text)
else:
    print(f"Ошибка при выполнении запроса. Код статуса: {result.status_code}")
    print(f"Текст ответа: {result.text}")