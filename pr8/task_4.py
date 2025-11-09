import requests

url = 'https://httpbin.org/get'
response = requests.get(url)

print(f"Статус-код: {response.status_code}")

if response.status_code == 200:
    print("Запит успішний!")

print("\n--- Заголовки відповіді ---")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print(f"\nТип вмісту: {response.headers['Content-Type']}")

print("\n--- Вміст (перші 100 символів) ---")
print(response.text[:100] + "...")
