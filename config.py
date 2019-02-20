import os

class Config:
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class TestingConfiguration(Config):
    TESTING = True
    DEBUG = True
    DATABASE_POLITICO = os.getenv("DATABASE_TEST_POLITICO_URL")

class DevelopmentConfiguration(Config):
    DEBUG=True
    DATABASE_POLITICO=os.getenv("DATABASE_POLITICO_URL")

class ProductionConfiguration(Config):
    DEBUG=False

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
    'production' : ProductionConfiguration,
}
