import pytest
import requests

from conftest import URL, REGULAR_LETTER_FIRST_NAME, REGULAR_LETTER_LAST_NAME, DOMESTIC_US_NUMBER, \
    updated_client_data, NEW_VALUE, MESSAGE_CLIENT_DELETED, SPECIFIC_LETTER_FIRST_NAME, SPECIFIC_LETTER_LAST_NAME, \
    PL_PREFIX_NUMBER, RANDOM_FIRST_NAME, RANDOM_LAST_NAME, RANDOM_NUMBER
from models import Client


@pytest.mark.smoke_test
def test_get_users(create_read_update_delete_request_headers):
    list_all_clients_request = requests.get(f"{URL}/clients", headers=create_read_update_delete_request_headers)
    list_all_clients_response_body = list_all_clients_request.json()

    assert list_all_clients_request.status_code == 200
    assert isinstance(list_all_clients_response_body["clients"], list), "Clients data should be stored in a list"


@pytest.mark.crud
@pytest.mark.parametrize(
    "first_name, last_name, phone",
    [
        (REGULAR_LETTER_FIRST_NAME, REGULAR_LETTER_LAST_NAME, DOMESTIC_US_NUMBER),
        (SPECIFIC_LETTER_FIRST_NAME, SPECIFIC_LETTER_LAST_NAME, PL_PREFIX_NUMBER),
        (RANDOM_FIRST_NAME, RANDOM_LAST_NAME, RANDOM_NUMBER),
    ],
)
def test_create_read_update_delete_user(first_name, last_name, phone, create_read_update_delete_request_headers):
    payload = Client(
        firstName=first_name,
        lastName=last_name,
        phone=phone
    )

    # Add new client
    add_new_client_request = requests.post(f"{URL}/client", headers=create_read_update_delete_request_headers,
                                           data=payload.json())

    assert add_new_client_request.status_code == 200

    add_new_client_response_body = add_new_client_request.json()
    returned_first_name = add_new_client_response_body["firstName"]
    returned_last_name = add_new_client_response_body["lastName"]
    returned_phone = add_new_client_response_body["phone"]
    client_id = add_new_client_response_body["id"]

    assert returned_first_name == first_name
    assert returned_last_name == last_name
    assert returned_phone == phone

    # Get client details
    get_client_details_request = requests.get(f"{URL}/client/{client_id}",
                                              headers=create_read_update_delete_request_headers)

    assert get_client_details_request.status_code == 200

    get_client_response_body = get_client_details_request.json()

    assert get_client_response_body == {
        "firstName": first_name,
        "lastName": last_name,
        "phone": phone,
        "id": client_id
    }

    # Update client - API doesn't allow to update firstName
    update_client_request = requests.put(f"{URL}/client/{client_id}", headers=create_read_update_delete_request_headers,
                                         data=updated_client_data.json())

    assert update_client_request.status_code == 200

    update_client_response_body = update_client_request.json()

    assert update_client_response_body == {
        "firstName": first_name,
        "lastName": NEW_VALUE,
        "phone": NEW_VALUE,
        "id": client_id
    }

    # Remove client
    remove_client_request = requests.delete(f"{URL}/client/{client_id}",
                                            headers=create_read_update_delete_request_headers)
    assert remove_client_request.status_code == 200

    remove_client_response_body = remove_client_request.json()

    assert remove_client_response_body == MESSAGE_CLIENT_DELETED
