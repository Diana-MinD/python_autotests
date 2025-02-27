import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f0f2a4751174544099a3c466773d1e15'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Мышь",
    "photo_id": 45
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name = {
    "pokemon_id": pokemon_id,
    "name": "Мышь2"
}

response_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)