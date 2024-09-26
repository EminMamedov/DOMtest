import pytest
import requests
import logging
from .settings import API_URL
from . import json


logging = logging.getLogger()


@pytest.fixture()
def post_pet_global():
    payload = json.payload
    response = requests.post(f'{API_URL}/pet', json=payload)
    logging.info(response.json())
    assert response.status_code == 200
    resp = response.json()
    assert resp['name'] == payload['name']
    assert resp['photoUrls'] == payload['photoUrls']
    pet_id = resp['id']
    yield pet_id
    requests.delete(f'{API_URL}/pet/{pet_id}')

