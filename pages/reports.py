import streamlit as st
import pandas as pd

from database import export_data

st.title("📊 Reports")

data = export_data()

if len(data) == 0:
    st.info("No Expense Data Found")

else:

    df = pd.DataFrame(
        data,
        columns=[
            "Date",
            "Reason",
            "Category",
            "Amount"
        ]
    )

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="RONI_Expense_Report.csv",
        mime="text/csv"
    )

    excel = df.to_excel(
        "RONI_Expense_Report.xlsx",
        index=False
    )

    with open("RONI_Expense_Report.xlsx", "rb") as f:

        st.download_button(
            label="⬇ Download Excel",
            data=f,
            file_name="RONI_Expense_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )