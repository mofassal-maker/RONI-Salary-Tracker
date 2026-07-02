import streamlit as st
import pandas as pd
from database import get_all_expenses, delete_expense

st.title("📜 Payment History")

data = get_all_expenses()

if not data:
    st.info("No Expense Found.")

else:
    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Date",
            "Reason",
            "Category",
            "Amount"
        ]
    )

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.success(f"Total Transactions : {len(df)}")

    st.divider()

    st.subheader("🗑️ Delete Expense")

    expense_id = st.selectbox(
        "Select Expense ID",
        df["ID"]
    )

    if st.button("Delete Selected Expense"):
        delete_expense(int(expense_id))
        st.success("Expense Deleted Successfully ✅")
        st.rerun()