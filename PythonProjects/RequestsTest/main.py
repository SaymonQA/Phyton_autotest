import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = ''ТОКЕН_СКРЫЛ'
header = {'Content-Type' : 'application/json' , 'trainer_token':token}
create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

rename_pokemon = {
    "pokemon_id": "72153",
    "name": "RENAMEpyton",
    "photo_id": 2
}

add_pokeball = {
    "pokemon_id": "72153"
}

'''response = requests.post(url = f'{URL}/pokemons' , headers = header, json = create_pokemon,)
print(response.text)'''

'''response_reName = requests.put(url = f'{URL}/pokemons' , headers = header, json = rename_pokemon,)
print(response_reName.text)'''

'''response_addPokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = header, json = add_pokeball,)
print(response_addPokeball.text)'''


