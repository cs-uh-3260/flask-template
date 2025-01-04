from abc import ABC

class BaseConfig(ABC):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/dev_db"


class ProductionConfig(BaseConfig):
    MONGO_URI = "mongodb://localhost:27017/prod_db"


class UnitTestConfig(BaseConfig):
    """
    Use mongomock for unit tests.
    """
    TESTING = True
    MONGO_URI = "mongomock://localhost"  # This signals we want mongomock.


class IntegrationTestConfig(BaseConfig):
    """
    Use a real MongoDB database for integration tests.
    (Requires a running instance of MongoDB.)
    """
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/test_db"
