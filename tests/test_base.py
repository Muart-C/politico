import unittest


from app import create_app
from api.admin.party.model import parties

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
        #a list of containing dictionaries containing parties
        self.parties = [
            {
                    "name" : "ANC",
                    "hqAddress" : "Kakamega",
                    "logoUrl" : "https://goo.gl/images/B9U4PK",
                },
                {
                    "name" : "Jubilee",
                    "hqAddress" : "Muthaiga",
                    "logoUrl" : "https://goo.gl/images/7hU72H",
                },
                {
                    "name" : "Maendeleo Chapchap",
                    "hqAddress" : "Machakos",
                    "logoUrl" : "https://goo.gl/images/3RKgQ6",
                }
        ]
        #an empty parties list for testing
        self.empty_parties_list = []

        #a dictionary containing an office
        self.office_with_data = {
            "name" : "ANC",
            "office_type" : "Kakamega",
        }

        #an office with empty fields
        self.office_with_empty_fields = {
            "name" : "",
            "office_type" : "",
        }
        #an office with a name of wrong data type
        self.party_with_name_of_wrong_data_type = {
            "name" : 4564,
            "office_type" : "Machakos",
            "logoUrl" : "https://goo.gl/images/3RKgQ6",
        }
        #a list of containing dictionaries containing offices
        self.offices = [
            {
                    "name" : "ANC",
                    "office_type" : "Kakamega",

                },
                {
                    "name" : "Jubilee",
                    "office_type" : "Muthaiga",

                },
                {
                    "name" : "Maendeleo Chapchap",
                    "office_type" : "Machakos",
                    "logoUrl" : "https://goo.gl/images/3RKgQ6",
                }
        ]
        #an empty offices list for testing
        self.empty_offices_list = []
    #clear the list to be empty
    def tearDown(self):
        self.parties.clear()