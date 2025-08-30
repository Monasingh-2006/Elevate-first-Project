import streamlit as st
import requests

# Set background image and styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌦️ Real-Time Weather App")

city = st.text_input("Enter a city name:", value="Delhi")

api_key = "a73d6fdb15168eb238665b18478b3fa5"  # Replace with your actual API key if needed

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None

if city:
    data = get_weather(city)
    if data:
        st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
        st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
        st.write(f"**Temperature:** {data['main']['temp']} °C")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
    else:
        st.error("City not found or API issue. Try another city.")
