import requests

def test_check_header():
    url = "https://playground.learnqa.ru/api/homework_header"

    response1 = requests.get(url)
    headers = response1.headers

    assert headers is not None, "There is no headers in the response"

    print(headers)

    assert "Date" in headers, "There is no header 'Date' in the response"
    assert "Content-Type" in headers, "There is no header 'HomeWork' in the response"
    assert "Content-Length" in headers, "There is no header 'Content-Type' in the response"
    assert "Connection" in headers, "There is no header 'Connection' in the response"
    assert "Keep-Alive" in headers, "There is no header 'Keep-Alive' in the response"
    assert "Server" in headers, "There is no header 'Server' in the response"
    assert "x-secret-homework-header" in headers, "There is no header 'x-secret-homework-header' in the response"
    assert "Cache-Control" in headers, "There is no header 'Cache-Controls' in the response"
    assert "Expires" in headers, "There is no header 'Expires' in the response"
