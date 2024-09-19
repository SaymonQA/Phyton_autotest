import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
token = 'ТОКЕН_СКРЫЛ'
header = {'Content-Type' : 'application/json' , 'trainer_token':token}
Trainer_id = '4831'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers' )
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'ESSENSE88'