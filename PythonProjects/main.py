import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3eeb1af465a95efd0382fa97e82eeef3'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}

body_pokeball = {
    "pokemon_id": "45034"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)'''

'''response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)'''



print(response_pokeball.text)


