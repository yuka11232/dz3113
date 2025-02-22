import requests

base = "https://fake-json-api.mock.beeceptor.com/"


endpoints = ["users", "posts", "comments", "products"]

for endpoint in endpoints:
    url = base + endpoint  
    try:
        response = requests.get(url) 
        if response.status_code == 200:
            print("Запрос к", url, "успешен!")
            print("Ответ:", response.json())
        else:
            print("Ошибка при запросе к", url, "Код статуса:", response.status_code)
    except Exception as e:
        print("Произошла ошибка при запросе к", url, "Ошибка:", e)