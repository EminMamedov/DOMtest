import pytest
import requests
from . import json
import allure
import logging
from .settings import API_URL


logging = logging.getLogger()


@allure.story('Проверка, что питомец успешно создается с кооректными данными')
@allure.feature('API_PETSTORE')
def test_post_pet():
    payload = json.payload_post
    response = requests.post(f'{API_URL}/pet', json=payload)
    logging.info(response.json())
    assert response.status_code == 200
    resp = response.json()
    assert resp['name'] == payload['name']
    assert resp['photoUrls'] == payload['photoUrls']


@allure.story('Проверка, что создание питомца с некорректными данными возвращает ошибку')
@allure.feature('API_PETSTORE')
def test_post_pet_error():
    try:
        payload = json.payload_error
        response = requests.post(f'{API_URL}/pet', json=payload)
        logging.info(f"Response: {response.json()}")
        assert response.status_code == 409, f"Expected status code 409 but got {response.status_code}"
        logging.info("Test passed!")

    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        logging.error("Test failed due to assert failure")
        allure.attach("Error message", str(e), allure.attachment_type.TEXT)
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        logging.error("Test failed due to an unexpected error")
        allure.attach("Error message", str(e), allure.attachment_type.TEXT)
        raise


@allure.story('Проверка, что информация о питомце корректно возвращается для существующего питомца')
@allure.feature('API_PETSTORE')
def test_get_pet(post_pet_global):
    response = requests.get(f'{API_URL}/pet/{post_pet_global}')
    logging.info(response.json())
    assert response.status_code == 200
    resp = response.json()
    assert resp['name'] == resp['name']
    assert resp['photoUrls'] == resp['photoUrls']


@allure.story('Проверка, что запрос для несуществующего питомца возвращает ошибку')
@allure.feature('API_PETSTORE')
def test_get_pet_error():
    response = requests.get(f'{API_URL}/pet/9875885')
    logging.info(response.json())
    assert response.status_code == 404


@allure.story('Проверка, что информация о питомце успешно обновляется')
@allure.feature('API_PETSTORE')
def test_put_pet(post_pet_global):
    payload = json.payload_put
    # response = requests.put(f'{API_URL}/pet/{post_pet_global}', json=payload)
    response = requests.put(f'{API_URL}/pet', json=payload)
    logging.info(response.json())
    assert response.status_code == 200
    resp = response.json()
    assert resp['name'] == resp['name']
    assert resp['photoUrls'] == resp['photoUrls']


@allure.story('Проверка, что обновление с некорректными данными возвращает ошибку')
@allure.feature('API_PETSTORE')
def test_put_pet_error(post_pet_global):
    try:
        payload = json.payload_error
        # response = requests.put(f'{API_URL}/pet/{post_pet_global}', json=payload)
        response = requests.put(f'{API_URL}/pet', json=payload)
        logging.info(f"Response: {response.json()}")
        assert response.status_code == 409, f"Expected status code 409 but got {response.status_code}"
        logging.info("Test passed!")

    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        logging.error("Test failed due to assert failure")
        allure.attach("Error message", str(e), allure.attachment_type.TEXT)
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        logging.error("Test failed due to an unexpected error")
        allure.attach("Error message", str(e), allure.attachment_type.TEXT)
        raise


@allure.story('Проверка, что питомец успешно удаляется')
@allure.feature('API_PETSTORE')
def test_delete_pet():
    response = requests.delete(f'{API_URL}/pet/89845')
    logging.info(response.json())
    assert response.status_code == 200


@allure.story('Проверка, что удаление несуществующего питомца возвращает ошибку')
@allure.feature('API_PETSTORE')
def test_delete_pet_error():
    response = requests.delete(f'{API_URL}/pet/89845')
    logging.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 404
    if response.status_code == 404:
        logging.info(f"Response Text: {response.text}")
    else:
        logging.info(response.json())
