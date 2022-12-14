import time   # to simulate a real time data, time loop
import numpy as np  
import pandas as pd  #read csv, df manipulation
import plotly.express as px  #interactive charts
import streamlit as st   # data web app development

st.set_page_config(
    page_title="Senior Project Dashboard",
    page_icon="👩‍🎓",
    layout="wide",
)

def refresher(seconds):
    dataset_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-muz2Bk67ZykK4qpwS5cXV8EomGeYOFKDJJH9l49jfHoZFUdDIKAAukdIYoMH5HA21aHD7NaRkFDU/pub?gid=0&single=true&output=csv"
    # read csv from a URL
    @st.experimental_memo
    def get_data() -> pd.DataFrame:
        return pd.read_csv(dataset_url)

    df = get_data()


    st.title("Bridge Protection System Real-Time Dashboard 🌉")

    # top-level filters
    Date_filter = st.selectbox("Select a Date", pd.unique(df["Date"]))



    dfDate = df[df["Date"] == Date_filter] #dataset of selected date
    AVGWeight = dfDate["Total_Weight_g"].mean()
    SNumCars = dfDate["Number_of_cars"].sum()

    # create three columns
    kpi1, kpi2 = st.columns(2)



    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Total Weight (g) Per Day 𐄷",
        value=round(AVGWeight),
        #delta=round((Total_Weight_g) - 10)
        )

    kpi2.metric(
        label="Total Number of cars Per Day 🚗 ",
        value=int(SNumCars),
        #delta=-10 + count_married,
    )

    DateAVGWeight = df.groupby('Date')[["Total_Weight_g"]].agg('mean')



    fig_col1, dataView = st.columns([3,2])

    with fig_col1:
        st.markdown("### Total Weight Per Hour ")
        fig = px.bar(data_frame=dfDate, y="Total_Weight_g", x="Time")
        st.write(fig)

    with dataView:
        st.markdown("### Data View")
        st.dataframe(df)
        time.sleep(seconds)

    fig_col2, fig_col3 = st.columns([2,2])
    with fig_col2:
        st.markdown("### Number of Vehicles Per Hour")
        fig2 = px.line(data_frame= dfDate, y= "Number_of_cars",x='Time', markers=True)
        st.write(fig2)

    with fig_col3:
        st.markdown("### AVG Total Weight (g) for each day")
        fig3 = px.line(data_frame=DateAVGWeight, y= "Total_Weight_g") #,x="Date"
        st.write(fig3)
        
refresher(1)


