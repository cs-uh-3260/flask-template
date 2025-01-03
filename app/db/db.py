import pymongo
import mongomock

# Note: see Flask's context management for an alternative implementation.
# Did not use it here because I thought it could abstract too much away.

class DatabaseClient:
    def __init__(self, uri):
        if uri.startswith("mongomock://"):
            self.client = mongomock.MongoClient()
        else:
            self.client = pymongo.MongoClient(uri)

    def get_db(self, db_name):
        return self.client[db_name]

# Global variable to hold the database client instance
db_client = None

def init_db(uri):
    global db_client
    db_client = DatabaseClient(uri)

def get_db():
    if db_client is None:
        raise Exception("Database client is not initialized. Call init_db(uri) first.")
    db_name = "test_db" if db_client.client.address == ("localhost", 27017) else "prod_db"
    return db_client.get_db(db_name)

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]
