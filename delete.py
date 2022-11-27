import db
from bson.objectid import ObjectId

def delete_db(id):
    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection["Cluster0"]
        collection = database["calorie"]
        try:
            collection.delete_one({"_id": ObjectId(id)})
            print('Delete sucessfully')
        except:
            print('Delete fail')

