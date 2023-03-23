import requests

endpoint = "http://localhost:8000/api/"

# response = requests.get(endpoint, params={'query': 123, 'next': 5}, json={'key': 'value'})
response = requests.post(endpoint, json={'name': 'Knight', 'hp': 5})

print(response.json())
print(response.status_code)