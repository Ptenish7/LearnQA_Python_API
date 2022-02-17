import requests

def test_check_cookies():
    url = "https://playground.learnqa.ru/api/homework_cookie"

    response1 = requests.get(url)
    cookies = response1.cookies.get_dict()

    assert cookies is not None, "There is no cookie in the response"

    print(cookies)

    assert "HomeWork" in cookies, "There is no cookie 'HomeWork' in the response"

