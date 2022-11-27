import db
from bson.objectid import ObjectId

def update_db(id, model:dict):
    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection["Cluster0"]
        collection = database["calorie"]
        try:
            collection.update_one({ "_id": ObjectId(id)}, { '$set': model})
            print('Update done')
        except:
            print('error on update')