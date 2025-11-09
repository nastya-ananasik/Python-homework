import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

url_ok = 'https://httpbin.org/status/200'
url_404 = 'https://httpbin.org/status/404' 
url_bad_domain = 'https://this-domain-does-not-exist-12345.com'

urls_to_test = [url_ok, url_404, url_bad_domain]

for url in urls_to_test:
    print(f"\n--- Спроба підключення до {url} ---")
    try:
        response = requests.get(url, timeout=5)

        response.raise_for_status()

        print(f"Успіх! Статус: {response.status_code}")
    
    except HTTPError as http_err:
        print(f"HTTP помилка: {http_err} (Статус: {http_err.response.status_code})")
    
    except ConnectionError as conn_err:
        print(f"Помилка з'єднання: {conn_err}")
    
    except Timeout:
        print("Помилка: Час очікування вийшов (Timeout)")

    except RequestException as e:
        print(f"Сталася помилка (RequestException): {e}")
