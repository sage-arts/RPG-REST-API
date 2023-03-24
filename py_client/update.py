import requests

endpoint = "http://localhost:8000/api/heros/5/update/"

data = {
    'name': 'Archer',
    'description': 'Aim god'
}

response = requests.put(endpoint, json=data)

print(response.json())
print(response.status_code)