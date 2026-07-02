import streamlit as st
from datetime import datetime
from database import save_salary, get_salary, get_total_expense

month = datetime.now().strftime("%B %Y")

st.title("🏠 Dashboard")

salary = get_salary(month)
expense = get_total_expense()
remaining = salary - expense

st.subheader(f"📅 {month}")

with st.expander("💰 Set Monthly Salary"):

    amount = st.number_input(
        "Enter Salary",
        min_value=0.0,
        step=100.0
    )

    if st.button("Save Salary"):
        save_salary(amount, month)
        st.success("Salary Saved Successfully")
        st.rerun()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Salary", f"৳{salary:,.0f}")
col2.metric("💸 Total Expense", f"৳{expense:,.0f}")
col3.metric("💵 Remaining", f"৳{remaining:,.0f}")