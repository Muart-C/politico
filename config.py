import os

class Config:
    """base class for configurations for all phases"""
    DEBUG = False


class TestingConfiguration(Config):
    """configuration for use during testing phase."""
    TESTING = False

class DevelopmentConfiguration(Config):
    """configurations for use during development phase."""
    DEBUG=True

app_config = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfiguration,
}

