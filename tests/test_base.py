import unittest


from app import create_app
from api.models.parties_model import PARTIES
from api.models.offices_model import OFFICES


class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        app = create_app("testing")
        self.client = app.test_client()
        #a dictionary containing a party
        self.party_with_data = {
            "name" : "ANC",
            "hqAddress" : "Kakamega",
            "logoUrl" : "https://goo.gl/images/B9U4PK",
        }


        self.second_party_with_data = {
            "name" : "ANC",
            "hqAddress" : "Kakamega",
            "logoUrl" : "https://goo.gl/images/B9U4PK",
        }
        #a party with empty fields
        self.party_with_empty_fields = {
            "name" : "",
            "hqAddress" : "",
        }
        #a party with a name of wrong data type
        self.party_with_name_of_wrong_data_type = {
            "name" : 4564,
            "hqAddress" : "Machakos",
            "logoUrl" : "https://goo.gl/images/3RKgQ6",
        }

        #a dictionary containing an office
        self.office_with_data = {
            "name" : "Presidency",
            "office_type" : "Office of the President",
        }
        self.OFFICES = []
        #an office with empty fields
        self.office_with_empty_fields = {
            "name" : "",
            "office_type" : "",
        }
        #an office with a name of wrong data type
        self.party_with_name_of_wrong_data_type = {
            "name" : 4564,
            "office_type" : "Machakos",
        }
        #a list of containing dictionaries containing offices

        #an empty offices list for testing
        self.empty_offices_list = []
    #clear the list to be empty
    def tearDown(self):
        PARTIES.clear()
        OFFICES.clear()