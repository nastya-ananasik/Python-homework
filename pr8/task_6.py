import requests

url = 'https://httpbin.org/html'
filename = 'page.html'

print(f"Завантажую сторінку з {url}...")

try:
    response = requests.get(url)
    response.raise_for_status() 

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)
        
    print(f"Успіх! Вміст збережено у файл {filename}")

except requests.RequestException as e:
    print(f"Не вдалося завантажити сторінку: {e}")
