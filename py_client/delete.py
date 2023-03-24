import requests

hero_id = input('Enter hero id\n')
try:
    hero_id = int(hero_id)
except:
    hero_id = None
    print(f'{hero_id} not valid')

if hero_id:
     endpoint = f"http://localhost:8000/api/heros/{hero_id}/delete/"

     response = requests.delete(endpoint)

     print(response.status_code)