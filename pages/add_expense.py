import streamlit as st
from datetime import date
from database import add_expense

st.title("➕ Add Expense")

amount = st.number_input(
    "💵 Amount",
    min_value=0.0,
    step=10.0
)

reason = st.text_input("📝 Reason")

category = st.selectbox(
    "📂 Category",
    [
        "Food",
        "Transport",
        "Rent",
        "Shopping",
        "Bills",
        "Family",
        "Education",
        "Medical",
        "Entertainment",
        "Other"
    ]
)

expense_date = st.date_input(
    "📅 Date",
    value=date.today()
)

if st.button("💾 Save Expense"):

    if amount <= 0:
        st.error("Enter a valid amount.")

    elif reason == "":
        st.error("Enter a reason.")

    else:
        add_expense(
            amount,
            reason,
            category,
            str(expense_date)
        )

        st.success("Expense Added Successfully ✅")