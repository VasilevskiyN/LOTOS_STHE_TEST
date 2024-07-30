import requests
import data
import time
import json

url = "http://192.168.1.145:8000/sthe/api/v2.0/db_clients"
api_key = "12345"


payload = {
    "sql": 'SELECT us_email FROM UEMS_Users WHERE us_id=:x',
    "module": " ",
    "params": {"x": 15}
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

print(response.json()['result'][0]['email'])