from tkinter.font import names

import configuration
from data import *
from  sender_stand_request import *
import data



def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body


def possitive_assert(name):
    token_x = grep_token(data.user_body)
    kit_body_x = get_kit_body(name)
    kit_body_response = post_new_client_kit(kit_body_x, token_x)

    assert kit_body_response.status_code == 201

def negative_assert_code_400(name):
    token_x = grep_token(data.user_body)
    kit_body_x = get_kit_body(name)
    kit_body_response = post_new_client_kit(kit_body_x, token_x)

    assert kit_body_response.status_code == 400


def test_create_kit_1_letter_in_name_get_success_response():
    possitive_assert("a")

def test_create_kit_511_letters_in_name_get_success_response():
    possitive_assert("Abcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabC")

def test_create_kit_ENG_letters_in_name_get_success_response():
    possitive_assert("QWErty")

def test_create_kit_RUS_letters_in_name_get_success_response():
    possitive_assert("Мария")

def test_create_kit_SPEC_letters_in_name_get_success_response():
    possitive_assert("№%")

def test_create_kit_space_in_name_get_success_response():
        possitive_assert("Человеки и КО")

def test_create_kit_numbers_in_name_get_success_response():
    possitive_assert("123")

def test_create_kit_numbers_to_STR_in_name_get_error_response():
    negative_assert_code_400(int(123))

def test_create_kit_more_512_letters_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcDg")

def test_create_kit_no_letters_in_name_get_error_response():
        negative_assert_code_400("")


def test_create_kit_no_params_in_name_get_error_response():
    token_x = grep_token(data.user_body)
    print(token_x)
    kit_body_0_response = post_new_client_kit_name_0(data.kit_body_0, token_x)
    print(data.kit_body_0, token_x)
    print(kit_body_0_response.json())
    assert (kit_body_0_response.status_code) == 400
