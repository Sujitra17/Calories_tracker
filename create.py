import db


def put_db(json):
    # store information in DB
    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection["Cluster0"]
        collection = database["calorie"]
        try:
            collection.insert_one(json)
            print('pushing success')
        except:
            print('pushing fail')
