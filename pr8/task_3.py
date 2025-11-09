import requests

url = 'https://httpbin.org/post'

login_data = {
    'username': 'my_test_user',
    'password': 'super_secure_pass123'
}

response = requests.post(url, data=login_data)

data = response.json()

print(f"Сервер отримав наші дані форми: {data['form']}")
