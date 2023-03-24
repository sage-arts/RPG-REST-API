import requests

endpoint = "http://localhost:8000/api/heros/"

data = {
    'name': 'Alchemist'
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)