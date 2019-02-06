import unittest


from app import create_app

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

        #a party with empty party name
        self.party_with_name_missing = {
            "name" : " ",
            "hqAddress" : "Kakamega",
            "logoUrl" : "https://goo.gl/images/B9U4PK",
        }

        #a party with empty party hq
        self.party_with_hq_missing = {
            "name" : "Jubilee",
            "hqAddress" : "Muthaiga",
            "logoUrl" : "https://goo.gl/images/7hU72H",
        }

        #a party with empty fields
        self.party_with_empty_fields = {
            "name" : " ",
            "hqAddress" : " ",
            "logoUrl" : " ",
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





