"""define app configurations"""
import os

class Config:
    """base class for configurations for all phases"""
    DEBUG = False


class TestingConfiguration(Config):
    """configuration for use during testing phase."""
    TESTING = True
    DEBUG = True
    DATABASE_POLITICO = os.getenv("DATABASE_TEST_POLITICO_URL")

class DevelopmentConfiguration(Config):
    """configurations for use during development phase."""
    DEBUG=True
    DATABASE_POLITICO=os.getenv("DATABASE_POLITICO_URL")

class ProductionConfiguration(Config):
    """configurations for use during production phase."""
    DEBUG=False

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
    'production' : ProductionConfiguration,
}

