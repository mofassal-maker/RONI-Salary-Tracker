import streamlit as st
from database import create_tables

st.set_page_config(
    page_title="RONI Salary Tracker",
    page_icon="💰",
    layout="wide"
)

create_tables()

st.title("💰 RONI Salary Tracker")
st.write("Welcome to RONI Salary Tracker")

st.info("⬅️ Use the left sidebar to open Dashboard, Add Expense, History and Reports.")