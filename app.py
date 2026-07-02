import streamlit as st
from database import create_tables

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="RONI Salary Tracker",
    page_icon="💰",
    layout="wide"
)

# ------------------------------
# Create Database
# ------------------------------
create_tables()

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.image("assets/logo.png", width=120)
st.sidebar.title("💰 RONI Salary Tracker")
st.sidebar.caption("Monthly Expense Manager")

# ------------------------------
# Home Page
# ------------------------------
st.title("💰 RONI Salary Tracker")

st.success("Welcome 👋")

st.markdown("""
### Features

✅ Dashboard

✅ Add Expense

✅ Payment History

✅ Reports

✅ Export CSV

✅ Export Excel

---

### How to Use

1. Dashboard → View Summary
2. Add Expense → Save Expenses
3. History → View/Delete Records
4. Reports → Download CSV/Excel

⬅️ Use the Sidebar to open each page.
""")

st.info("Made with ❤️ by Mofassal Roni")