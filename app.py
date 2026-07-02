import streamlit as st
from database import create_tables

# Create database tables
create_tables()

# Page Config (Only Once)
st.set_page_config(
    page_title="RONI Salary Tracker",
    page_icon="💰",
    layout="wide"
)

# Sidebar
st.sidebar.title("💰 RONI Salary Tracker")
st.sidebar.write("Monthly Expense Manager")

st.title("💰 RONI Salary Tracker")

page = st.sidebar.selectbox(
    "📋 Menu",
    [
        "Dashboard",
        "Add Expense",
        "History",
        "Reports"
    ]
)

if page == "Dashboard":
    from pages.dashboard import *

elif page == "Add Expense":
    from pages.add_expense import *

elif page == "History":
    from pages.history import *

elif page == "Reports":
    from pages.reports import *