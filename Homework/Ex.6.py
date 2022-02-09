import requests

url = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(url)
all_responses = response.history

amount_of_responses = len(all_responses)
print(f"There was {amount_of_responses} redirects")

last_response = response.history[amount_of_responses - 1]
print(f"The last of redirects is {last_response.url}")