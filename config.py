"""define app configurations"""
import os

class Config:
    """base class for configurations for all phases"""
    DEBUG = False
    DATABASE_HOST=os.getenv("DATABASE_HOST")
    DATABASE_PORT=os.getenv("DATABASE_PORT")
    DATABASE_USERNAME=os.getenv("DATABASE_USERNAME")
    DATABASE_POLITICO=os.getenv("DATABASE_POLITICO")


class TestingConfiguration(Config):
    """configuration for use during testing phase."""
    TESTING = True
    DEBUG = True
    DATABASE_POLITICO_TEST = os.getenv("DATABASE_POLITICO_TEST")

class DevelopmentConfiguration(Config):
    """configurations for use during development phase."""
    DEBUG=True
    DATABASE_URL = os.getenv("DATABASE_URL")

class ProductionConfiguration(Config):
    """configurations for use during production phase."""
    DEBUG=False

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
    'production' : ProductionConfiguration,
}

