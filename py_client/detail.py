import requests

endpoint = "http://localhost:8000/api/heros/1/"
response = requests.get(endpoint)

print(response.json())
print(response.status_code)