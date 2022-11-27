import db
import pandas as pd

def get_db():
    # store information in DB

    iden = []
    date = []
    time = []
    food_item = []
    food_cat = []
    cal = []

    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection["Cluster0"]
        collection = database["calorie"]
        for data in collection.find():
            iden.append(data['_id'])
            date.append(data["date"])
            time.append(data['time'])
            food_item.append(data['food item'])
            food_cat.append(data["food cat"])
            cal.append(data['cal'])
        
        for_df = {
                  'date': date,
                  'time':time,
                  'food_item': food_item,
                  'food_cat': food_cat,
                  'cal': cal
                  }
        df = pd.DataFrame(for_df, index=iden)
        return df