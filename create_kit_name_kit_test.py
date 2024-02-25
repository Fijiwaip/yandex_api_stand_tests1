import sender_stand_request
import data


def get_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body['name'] = name

    return kit_body


def get_empty_kit_body():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')

    return kit_body

def positive_assert(name):
    token = get_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()['name'] == name


def negative_assert(name):
    token = get_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 400



def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")



def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")



def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert("")



def test_create_kit_16_letter_in_name_get_error_response():
    negative_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")



def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")



def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")



def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")



def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")



def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")



def test_create_kit_no_name_get_error_response():
    token = get_token()
    kit_body = get_empty_kit_body()
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 400


def test_create_kit_number_type_name_get_error_response():
    negative_assert(123)