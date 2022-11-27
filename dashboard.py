import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import get


@st.cache(allow_output_mutation=True)
def load_mongo():
    df = get.get_db()
    return df

def render():
    #load data
    df = load_mongo()
    df['new_date'] = df['date']+" "+df['time']
    df['new_date'] = pd.to_datetime(df['new_date'], format='%Y-%m-%d %H:%M:%S')
    # Header
    st.title('Calories Tracking Dashboard')


    #calculation

    monthly_data = df.groupby(by=[df.new_date.dt.month])['cal'].sum()
    Total_this_month = monthly_data.iloc[1]
    Total_last_month = monthly_data.iloc[2]
    diff_from_last_month = Total_this_month - Total_last_month

    daily_data = df.groupby(by=[df.date])['cal'].sum()
    today = daily_data[-1]
    yesterday = daily_data[-2]
    diff_from_yesterday = today - yesterday

    # KPI

    col1, col2 = st.columns(2)
    col1.metric("Monthly Calorie",Total_this_month, "{} Calorie from last month".format(diff_from_last_month))
    col2.metric("Total Calorie today",today, "{} Calorie from yesterday".format(diff_from_yesterday))

    # controller
    # pick time period
    # pick data range as 1 month, 1 week or no filter


    # another colume
    col3, col4 = st.columns(2)

    #pie chart
    # calorie by food cat
    pie_data = df.groupby('food_cat')['cal'].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(2.5, 5))
    ax.pie(pie_data, labels=pie_data.index, autopct='%.1f%%')
    col3.pyplot(fig)

    # line chart

    #calculate sum of values, grouped by week
    line_data = df.groupby([pd.Grouper(key='new_date', freq='W')])['cal'].sum()
    col4.line_chart(line_data)

    # Bar chart

    bar_data = df[['date', 'time', 'cal']]
    bar_data['date'] = pd.to_datetime(df['date'])
    bar_chart_input = pd.pivot_table(bar_data, values='cal', columns=['time'], index= ['date'])
    st.bar_chart(bar_chart_input)




