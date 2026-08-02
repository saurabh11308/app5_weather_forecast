import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for next days")
city = st.text_input("Place",placeholder="Enter City name",)
days = st.slider("Forecast days",help="Enter the number of days fpr which "
                                      "you wannt to predict",min_value=1,
                 max_value=5)
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.write(f"{option} for the next {days} days in {city}")
try:
    if city:
        data = get_data(city,days)
        dates = [d['dt_txt'] for d in data]
        if option == "Temperature":
            temperature = [t['main']['temp']/10 for t in data]
            figure = px.line(x=dates,y=temperature,labels={'x':"Date",'y':"Temperature("
                                                                          "C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            sky = [s['weather'][0]['main'] for s in data]
            image_repo = {"Clear":"images/clear.png",
                          "Clouds":"images/cloud.png",
                          "Rain":"images/rain.png",
                          "Snow":"images/snow.png"}
            sky_image = [image_repo[s] for s in sky]
            st.image(sky_image,width=115)
except KeyError:
    st.write("The place doesnt exist")