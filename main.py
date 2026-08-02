import streamlit as st
import plotly.express as px

st.title("Weather forecast for next days")
city = st.text_input("Place",placeholder="Enter the city")
days = st.slider("Forecast days",help="Enter the number of days fpr which "
                                      "you wannt to predict",min_value=1,
                 max_value=5)
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.write(f"{option} for the next {days} days in {city}")
dates = ["01-08-2026","02-08-2026","03-08-2026"]
temperature = [10,14,17]
temperature = [i*days for i in temperature]
figure = px.line(x=dates,y=temperature,labels={'x':"Date",'y':"Temperature("
                                                              "C)"})
st.plotly_chart(figure)