import streamlit as st
import pandas as pd
import get
import datetime
import delete


@st.cache(allow_output_mutation=True)
def load_mongo():
    df = get.get_db()
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
        st.write('please select data id to delete')


    st.subheader('Deleted record')

    # submit
    if st.button('Submit'):
        delete.delete_db(selected_id)
        st.warning('Delete data success')