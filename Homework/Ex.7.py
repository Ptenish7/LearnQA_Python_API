import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

types_query = ["GET", "POST", "PUT", "DELETE"]
types_query2 = ["OPTIONS", "HEAD", "PATCH"]

methods = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]
m = {"method":"GET"}

responses_without_params = [requests.get(url), requests.post(url), requests.put(url), requests.delete(url)]
responses_without_params2 = [requests.options(url), requests.head(url),  requests.patch(url)]
responses_pozitiv = [requests.get(url, params={"method":"GET"}), requests.post(url, data={"method":"POST"}), requests.put(url, data={"method":"PUT"}), requests.delete(url, data={"method":"DELETE"})]


print("1. Вывод в случае запроса любого типа без параметра:")
n = 0
for i in responses_without_params:
        result = i
        print(f" Запрос c типом {types_query[n]} к URL  {result.url} завершен с сообщением '{result.text}' и статус-кодом {result.status_code}")
        n = n + 1

print("2. Вывод в случае запросов с другими типами:")
k = 0
for i in responses_without_params2:
        result = i
        print(f" Запрос c типом {types_query2[k]} к URL  {result.url} завершен с сообщением '{result.text}' и статус-кодом {result.status_code}")
        k = k + 1

print("3. Вывод в случае запросов с правильным значением method:")
j = 0
for i in responses_pozitiv:
        result = i
        print(f" Запрос c типом и методом {types_query[j]} к URL  {result.url} завершен с сообщением '{result.text}' и статус-кодом {result.status_code}")
        j = j + 1

print("4. Вывод в случае всех возможных сочетаний реальных типов запроса и значений параметра method:")
for m in methods:
        responses = [requests.get(url, params=m), requests.post(url, data=m), requests.put(url, data=m),
                     requests.delete(url, data=m)]
        for r in responses:
                result = r
                print(f" Запрос к URL  {result.url} завершен с сообщением '{result.text}' и статус-кодом {result.status_code}{m}")

print("Тип запроса не совпадает со значением параметра, но ответ от сервера положительный для следующего запроса:")
response = requests.delete(url, data={"method":"GET"})
print(f"{types_query[3]}-запрос с {methods[0]} даёт ответ {response.text}")
