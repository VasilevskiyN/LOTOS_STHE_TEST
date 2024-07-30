import requests
import data
import time
import json

url = "http://192.168.1.145:8000/sthe/api/v2.0/db_clients"
api_key = "12345"
payload = {
    "sql": 'SELECT us_email FROM UEMS_Users',
    "module": " ",
    "params": {}
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
response = response.json()


def DB_run(db_conn, sql, module='', params={}):
    print(type(params), params)
    print(type(sql), sql)
    return ''
    with Session(db_conn) as session:
        res = session.execute(text(sql), params)
    if 'INSERT' in sql:
        return res.lastrowid
    else:
        rows = res.fetchall()
        return rows