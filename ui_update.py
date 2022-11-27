import streamlit as st
import pandas as pd
import get
import datetime
import update
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
    #load data
    df = load_mongo()
    df['date'] = df['date'].astype(str)
    df['Date'] = df['date']+" "+df['time']
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
    earliest = df['Date'].min()
    latest = df['Date'].max()
    col1, col2 = st.columns(2)
    start = col1.date_input('start date', earliest)
    end = col2.date_input('end date', latest)
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    df = df[df['Date'] >= start]
    df = df[df['Date'] <= end]
    show_df = df[['Date', 'food_item', 'food_cat', 'cal']]
    show_df = show_df.sort_values(by='Date',ascending=True)
    # Header
    st.title('Calories Tracking  input')
    # table of items
    st.dataframe(show_df)

    # multi section bar

    selected_indices = st.multiselect('Select rows:', show_df.index, max_selections=1)
    # Text for Post
    try:
        selected_id = selected_indices[0]
        selected_row = show_df.loc[selected_id, :]
        st.write(selected_row)
    except:
        st.write('please select data id to update')


    st.subheader('Update record')

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
        update.update_db(selected_id, data)
        st.warning('Update data success')