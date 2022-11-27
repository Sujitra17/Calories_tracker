from pymongo import MongoClient

with open('key.txt') as f:
    key = f.read()
Mongo_secret = key

class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(Mongo_secret)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()