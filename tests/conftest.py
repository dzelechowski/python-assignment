import os

import pytest
import requests
from faker import Faker

from models import Client

BASIC_AUTH = os.getenv('BASIC_AUTH')
DOMESTIC_US_NUMBER = "(111) 111-1111"
fake = Faker()
MESSAGE_CLIENT_DELETED = {
    "message": "client deleted"
}
NEW_VALUE = "New"
PL_PREFIX_NUMBER = "+48 111 111 111"
RANDOM_FIRST_NAME = fake.first_name()
RANDOM_LAST_NAME = fake.last_name()
RANDOM_NUMBER = fake.phone_number()
REGULAR_LETTER_FIRST_NAME = "John"
REGULAR_LETTER_LAST_NAME = "Smith"
SPECIFIC_LETTER_FIRST_NAME = "Łucja"
SPECIFIC_LETTER_LAST_NAME = "Hämäläinen"
updated_client_data = Client(
    firstName=NEW_VALUE,
    lastName=NEW_VALUE,
    phone=NEW_VALUE
)
URL = "https://qa-interview-api.migo.money"


@pytest.fixture
def get_token_request_headers():
    return {
        "User-Agent": "PY",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": BASIC_AUTH
    }


@pytest.fixture
def create_read_update_delete_request_headers(get_api_key):
    return {
        "X-API-Key": get_api_key,
        "User-Agent": "PY",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br"
    }


@pytest.fixture
def get_api_key(get_token_request_headers):
    token_request = requests.post(f"{URL}/token", headers=get_token_request_headers)
    assert token_request.status_code == 200
    token_request_response_body = token_request.json()
    token = token_request_response_body["key"]
    return token
