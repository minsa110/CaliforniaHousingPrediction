# TO TEST: streamlit run app.py
# 28060 Sea Lane Drive
# 16401 Calle Feliz
# 1201 Tower Grove Drive

import streamlit as st
import pickle
import numpy as np
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static

st.set_page_config(
     page_title="Caliornia Housing Price Prediction",
     page_icon="🏠"
)

model = pickle.load(open('model.pkl','rb'))

def predict_price(longitude,latitude,total_bedrooms,median_income,ocean_proximity, pop_per_hhold, total_rooms, rooms_per_hhold, bedrooms_per_room, housing_median_age, population, NEAR_OCEAN, NEAR_BAY, less1H_OCEAN, INLAND, ISLAND):
    input=np.array([[longitude,latitude,total_bedrooms,median_income,ocean_proximity, pop_per_hhold, total_rooms, rooms_per_hhold, bedrooms_per_room, housing_median_age, population, NEAR_OCEAN, NEAR_BAY, less1H_OCEAN, INLAND, ISLAND]]).astype(np.float64)
    prediction = model.predict(input)
    
    return int(prediction)

def dollar_value(number):
    return ("$" + "{:,}".format(number))

def main():
    # st.title("California Housing Prediction")
    html_title = """
    <div style="background:#C06C84 ;padding:10px">
    <h2 style="color:white;text-align:center">Predict Home Price in California</h2>
    </div>

    <p>Enter information for a home in California to predict its price (<b>pretend it's 1990</b> 😉).</p>
    """
    st.markdown(html_title, unsafe_allow_html = True)

    address = st.text_input("Street address")

    total_bedrooms = st.text_input("Number of bedrooms")
    total_bathrooms = st.text_input("Number of bathrooms")

    loc_option = st.selectbox(
        'Which of the following apply to the home?',
        ('Near ocean', 'Inland', 'Island'))

    if loc_option == 'Near ocean':
        NEAR_OCEAN = 1
        INLAND = 0
        ISLAND = 0

    if loc_option == 'Inland':
        NEAR_OCEAN = 0
        INLAND = 1
        ISLAND = 0

    if loc_option == 'Island':
        NEAR_OCEAN = 0
        INLAND = 0
        ISLAND = 1

    if st.button("Predict the price"):
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(address)

        longitude = location.longitude
        latitude = location.latitude

        # median defaults as to not have too many input boxes
        median_income = 3.87
        pop_per_hhold = 2.85
        # total_rooms = 20
        total_rooms = int(total_bathrooms) + int(total_bedrooms)
        rooms_per_hhold = total_rooms / pop_per_hhold
        bedrooms_per_room = int(total_bedrooms) / total_rooms
        housing_median_age = 29
        population = 1426
        ocean_proximity = 0
        less1H_OCEAN = 0
        NEAR_BAY = 0

        output = predict_price(longitude,latitude,total_bedrooms,median_income,ocean_proximity, pop_per_hhold, total_rooms, rooms_per_hhold, bedrooms_per_room, housing_median_age, population, NEAR_OCEAN, NEAR_BAY, less1H_OCEAN, INLAND, ISLAND)
        st.success('The predicted price for this house is {}'.format(dollar_value(output)))

        st.markdown(location.address + " *(Latitude: " + str(round(location.latitude, 2)) + " Longitude: " + str(round(location.longitude, 2)) +")*")

        california = folium.Map(location=[36.778259, -119.417931], zoom_start=5)
        folium.Marker(location=[latitude, longitude ], popup=address, tooltip=address).add_to(california)

        folium_static(california)

if __name__=='__main__':
    main()