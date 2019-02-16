import unittest


from app import create_app
from config import app_config
from api.models.parties_model import Party
from api.models.offices_model import Office
from api.database.db_manage import drop_data_from_tables
class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        self.app = create_app("testing")
        with self.app.app_context():
            self.client = self.app.test_client()

    #clear the list to be empty
    def tearDown(self):
        drop_data_from_tables()
