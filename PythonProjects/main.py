"""
AvtotestPython
"""
import requests

URL = "https://api.pokemonbattle.me"
HEADERS = {"Content-Type": "application/json", "trainer_token": "447a771e036b9281776a0dda9e750b56"}

BODY = {"name": "generate", "photo": "generate"}

response = requests.post(url=f'{URL}/v2/pokemons', json=BODY, headers=HEADERS)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()}')

URL = "https://api.pokemonbattle.me"
HEADERS = {"Content-Type": "application/json", "trainer_token": "447a771e036b9281776a0dda9e750b56"}

BODY = {"pokemon_id": "16473", "name": "New Nam", "photo": "generate"}
response = requests.put(url=f'{URL}/v2/pokemons', json=BODY, headers=HEADERS)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()}')

URL = "https://api.pokemonbattle.me"
HEADERS = {"Content-Type": "application/json", "trainer_token": "447a771e036b9281776a0dda9e750b56"}

BODY = {"pokemon_id": "16475"}
response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', json=BODY, headers=HEADERS)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()}')

URL = "https://api.pokemonbattle.me"
HEADERS = {"Content-Type": "application/json",}
PARAMS = {"trainer_id": "2553"}
response = requests.get(url=f'{URL}/v2/trainers', params=PARAMS, headers=HEADERS)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()}')

