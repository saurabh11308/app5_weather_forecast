from cProfile import label

import streamlit as st
from  backend import get_data
import plotly.express as px

st.title("Weather Forecast for the Next Days")
city = st.text_input(label="Place",placeholder="Enter city name :-")
days = st.slider(label="Forecast days",min_value=1,max_value=5,
                         help="Please select a value between 1 and 5")
type = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{type} for the next {days} days in {city}")

date = ["2026-20-07","2026-19-07","2026-18-07"]
temprature = [6,7,15]
temprature = [days*i for i in temprature]

figure = px.line(x=date,y=temprature,labels={"x":"Dates","y":"Tempratures ("\
                                                             "C)"})
st.plotly_chart(figure)