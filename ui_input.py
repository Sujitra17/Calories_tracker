import streamlit as st
import pandas as pd
import get
import datetime
import create
import model


@st.cache(allow_output_mutation=True)
def load_mongo():
    df = get.get_db()
    return df


@st.cache
def load_collection():
    df = pd.read_csv('collection.csv')
    return df

def render():
    # Text for Post
    st.subheader('Create new record')

    collection = load_collection()
    col3, col4 = st.columns(2)
    food_cat_list = collection['FoodCategory'].unique().tolist()
    food_cat = col3.selectbox(
        "Select food category",
        food_cat_list
    )
    seleted_item = collection[collection['FoodCategory'] == food_cat]
    food_item_list = seleted_item['FoodItem'].unique().tolist()
    food_item = col4.selectbox(
        "Select food item",
        food_item_list
    )
    cal_row = collection[collection['FoodItem'] == food_item]
    cal = cal_row.iloc[0,2]


    st.write('you select {a} , {b}. total calories will be {c} calories'.format(a = food_cat, b= food_item, c=cal))

    col5, col6 = st.columns(2)
    date_input = col5.date_input('Record date', datetime.datetime.now())
    input_time = col6.time_input('Record time', datetime.datetime.now())


    data = model.data_model(
        date=str(date_input),
        time=str(input_time),
        food_item=food_item,
        food_cat=food_cat,
        cal=float(cal)
    )

    # submit
    if st.button('Submit'):
        create.put_db(data)
        st.warning('Upload data success')