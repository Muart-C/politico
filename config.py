import os

class Config:
    DEBUG = False


class TestingConfiguration(Config):
    TESTING = True
    DEBUG = True
    DATABASE_POLITICO = os.getenv("DATABASE_POLITICO_TEST_LOCAL")

class DevelopmentConfiguration(Config):
    DEBUG=True
    DATABASE_POLITICO=os.getenv("DATABASE_POLITICO_DEV")

class ProductionConfiguration(Config):
    DEBUG=False
    DATABASE_POLITICO=os.getenv('DATABASE_POLITICO_URI')

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
    'production' : ProductionConfiguration,
}
