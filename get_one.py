import db
from bson.objectid import ObjectId

def get_one_db(id):
    # store information in DB
    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection["Cluster0"]
        collection = database["calorie"]
        data = collection.find_one({ "_id": ObjectId(id)})
        return data