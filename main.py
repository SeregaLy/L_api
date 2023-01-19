import requests

params = {"q" : "fanny cats"}
response = requests.get('https://google.com/serch', params=params)

print(response.headers)
print(response.text)