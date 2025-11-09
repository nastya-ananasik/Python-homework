import requests

url = 'https://youtube.com/results'

response = requests.get(url, params={'v': 'znfxnCgBD6Q'})

print(response)
