import os

class Config:
    DEBUG = False


class TestingConfiguration(Config):
    TESTING = True
    DEBUG = True
    DATABASE_POLITICO = os.getenv("DATABASE_TEST_POLITICO_URL")

class DevelopmentConfiguration(Config):
    DEBUG=True
    DATABASE_POLITICO=os.getenv("DATABASE_POLITICO_URL")

class ProductionConfiguration(Config):
    DEBUG=False
    DATABASE_POLITICO_URI=os.getenv('DATABASE_POLITICO_URI')

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
    'production' : ProductionConfiguration,
}
