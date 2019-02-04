class Config(object):
    """base class for configurations for all phases"""
    DEBUG = False


class TestingConfiguration(Config):
    """configuration for use during testing phase."""
    TESTING = False

class DevelopmentConfig(Config):
    """configurations for use during development phase."""

app_configuration = {
    'testing': TestingConfiguration,
    'development' : DevelopmentConfig,
}

