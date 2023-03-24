import requests

endpoint = "http://localhost:8000/api/heros/1573498579/"
response = requests.get(endpoint)

print(response.json())
print(response.status_code)