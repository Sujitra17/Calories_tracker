

def data_model(date:str, time:str, food_item:str, food_cat:str, cal:float):
    json = {
        'date': date,
        'time': time,
        'food item': food_item,
        'food cat': food_cat,
        'cal': cal
    }

    return json