import pytest
import requests

URL = "https://api.pokemonbattle.me:"
HEADERS = {"Content-Type": "application/json"}

def test_get_trainers_200():
    """
    KTI-1. Get my trainer name
    """
    response = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id': 2553}, headers=HEADERS)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():
    """
    KTI-2. Get trainers by id
    """
    response = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id': 2553}, timeout= 2)
    assert response.status_code == 200, 'Unexpected status code'
    assert response.json()['data'][0]['trainer_name'] == 'Владимир'
