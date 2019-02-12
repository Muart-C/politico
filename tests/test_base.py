import unittest


from app import create_app
from api.models.parties_model import PARTIES
from api.models.offices_model import OFFICES


class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        app = create_app("testing")
        self.client = app.test_client()

    #clear the list to be empty
    def tearDown(self):
        PARTIES.clear()
        OFFICES.clear()