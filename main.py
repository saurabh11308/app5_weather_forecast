import streamlit as st


st.title("Weather forecast for next days")
city = st.text_input("Place",placeholder="Enter the city")
days = st.slider("Forecast days",help="Enter the number of days fpr which "
                                      "you wannt to predict",min_value=1,
                 max_value=5)
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.write(f"{option} for the next {days} days in {city}")
