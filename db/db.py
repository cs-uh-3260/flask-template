from pymongo import MongoClient

mongo_client = None
demo_db = "DEMO_DB"


def get_db_client():
    global mongo_client
    if not mongo_client:
        mongo_client = MongoClient()  # defaults to localhost:27017
    return mongo_client


def get_db():
    client = get_db_client()
    return client[demo_db]
