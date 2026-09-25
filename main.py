import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client() 
st.set_page_config(
    page_title="Travel Assistant",
    page_icon="✈️",
    layout="wide"
)

# st.title("🌍 Travel Assistant✈️")

import streamlit as st

st.set_page_config(page_title="Travel Assistant", layout="wide")

BANNER_URL = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1600&q=80"

st.markdown(
    f"""
    <div style="
        background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.65)),
                    url('{BANNER_URL}');
        background-size: cover;
        background-position: center;
        padding: 55px 30px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
    ">
        <h1 style="margin: 0; font-size: 2.6rem;">🌍 Travel Assistant✈️</h1>
        <p style="margin: 8px 0 0 0; font-size: 1.15rem; color: #e2e8f0;">
            Plan your next journey, explore hidden spots, and build custom itineraries.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st

st.set_page_config(page_title="Travel Assistant", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #e0f2fe 0%, #f0fdf4 50%, #fefce8 100%);
        background-attachment: fixed;
        color: #1e293b;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.caption ("Your 24/7 digital travel concierge")
name = st.text_input("Enter Your Name")
destination= st.text_input(f"Where You want to go {name}")
days= st.number_input("How many days of trip you want ", min_value= 1 , max_value=30)

budget = st.selectbox("Select Budget" , ["Luxury","Modrate","Budgeted"])
travel_type = st.selectbox("Select Type" , ["Family","Friends","Solo"])
prompt = f""""You are Travel Planner User Want to go {destination} with budget type {budget}
and {name} is planing trip as {travel_type} trip 
and for {days} , Give a tripo and share answer in Bullet format """



if st.button("Plan Trip"):
    st.write("Your Destination is", destination)
    st.write("Number of Days ", days)
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
            )

    with st.spinner("Wait for it ..." , show_time= True):
        time.sleep(5)
    st.write("Here Are Some Fab Suitable Spots For U")
    st.write(interaction.output_text)
    st.success("Happy Vacation")