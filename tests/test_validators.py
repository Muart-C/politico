import unittest
from flask import request
from api.utils.validator import sanitize_input, validate_string_data_type, check_is_valid_url, check_json_party_keys
from api.utils.validator import validate_int_data_type, return_response

class TestValidators(unittest.TestCase):
    def test_sanitize_input(self):
        self.assertEqual(sanitize_input("*`92 "), False)

    def test_validate_string_data_type(self):
        self.assertEqual(validate_string_data_type("name"), True)

    def test_is_valid_url(self):
        self.assertEqual(check_is_valid_url("https://goo.gl/images/3RKgQ6"), True)

    def test_validate_int_data_type(self):
        self.assertEqual(validate_int_data_type(343), True)
