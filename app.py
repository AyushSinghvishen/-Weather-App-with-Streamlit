import streamlit as st
from weather import get_weather

st.set_page_config(page_title="🌦️ Weather Dashboard", layout="centered")

st.title("🌍 Live Weather App")
st.write("Get current weather data for any city in the world!")

# City input
city = st.text_input("Enter city name:", "London")

if st.button("Get Weather"):
    weather = get_weather(city)
    if weather:
        st.success(f"Weather in {weather['city']}:")
        st.metric("🌡️ Temperature (°C)", f"{weather['temperature']}°C")
        st.metric("💧 Humidity (%)", f"{weather['humidity']}%")
        st.metric("🌬️ Wind Speed (m/s)", f"{weather['wind']}")
        st.write(f"**Condition:** {weather['description']}")
    else:
        st.error("❌ Could not fetch data. Check city name or API key.")

# Extra feature: multiple cities
st.subheader("🌐 Compare Multiple Cities")
cities = st.text_area("Enter multiple cities (comma separated):", "London, Paris, Tokyo")
if st.button("Compare"):
    city_list = [c.strip() for c in cities.split(",")]
    for c in city_list:
        weather = get_weather(c)
        if weather:
            st.write(f"**{weather['city']}** → {weather['temperature']}°C | {weather['description']}")
        else:
            st.write(f"⚠️ No data for {c}")
