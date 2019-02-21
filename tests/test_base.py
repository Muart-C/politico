import unittest


from app import create_app
from config import app_config
from api.models.parties_model import Party
from api.models.offices_model import Office
from api.database.database import DatabaseSetup

class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        with self.app.app_context():
            DatabaseSetup().drop_tables_if_exists()
            DatabaseSetup().create_all_tables()
            DatabaseSetup().create_admin_if_does_not_exist()
