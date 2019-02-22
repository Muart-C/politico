import unittest
from app import create_app


class TestDevelopmentConfiguration(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')

    def test_app_is_development(self):
        self.assertEqual(self.app.config['DEBUG'], True)

    def tearDown(self):
        self.app = None


class TestTestingConfiguration(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
    def test_app_is_testing(self):
        self.assertEqual(self.app.config['DEBUG'], True)
        self.assertEqual(self.app.config['TESTING'], True)
    def tearDown(self):
        self.app = None

class TestProductionConfiguration(unittest.TestCase):
    def setUp(self):
        self.app = create_app('production')
    def test_app_is_production(self):
        self.assertEqual(self.app.config['DEBUG'], False)

    def tearDown(self):
        self.app = None