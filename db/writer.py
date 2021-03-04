from pymongo import MongoClient
from db.db_config import *


def writer(func):
    def insert_to_db(arg):
        with MongoClient(HOST, PORT) as client:
            db = client[RES_DB]
            collection = db[RES_COL]
            result = func(arg)
            collection.insert_many(result)
            return func(arg)
    return insert_to_db
