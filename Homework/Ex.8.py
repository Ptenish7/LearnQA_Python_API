import requests
import json
import time

token = "token"
seconds = "seconds"
status = "status"
result = "result"

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
obj = json.loads(response.text)
print(f"Задача создана: {obj}")


if token in obj:
    token = (obj[token])
else:
    print(f"Ключа {token} в JSON нет")

if seconds in obj:
    seconds = (obj[seconds])
else:
    print(f"Ключа {seconds} в JSON нет")

response2 = requests.get(url, params={"token":f"{token}"})
obj2 = json.loads(response2.text)
print(f"Первый запрос с токеном: {obj2}")
status2 = (obj2[status])

if status2 == "Job is NOT ready":
    time.sleep(seconds)
    response3 = requests.get(url, params={"token": f"{token}"})
    obj3 = json.loads(response3.text)
    status2 = (obj3[status])
else:
    print("Job in other status")

if status2 == "Job is ready" and result in obj3:
    print(f"Второй запрос с токеном: {obj3}")
else:
    print("Job is NOT ready")
