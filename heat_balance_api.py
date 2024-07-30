import requests
import data

url = "http://192.168.1.145:8000/task_create"

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

print(response.json())
