import streamlit as st
import requests
import json

st.title("Bank Churn Model UI")
with st.form("ChurnForm"):
    Age = st.number_input("Age", key="age")
    Balance = st.number_input("Balance", key="balance")
    EstimatedSalary = st.number_input("EstimatedSalary", key="salary")
    Gender = st.text_input("Gender", key="gender")
    Geography = st.text_input("Geography", key="geography")
    IsActiveMember = st.selectbox("IsActiveMember", (0, 1))
    NumOfProducts = st.number_input("NumOfProducts", key="products")
    Tenure = st.number_input("Tenure", key="tenure")
    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "Age_censored": Age,
            "EstimatedSalary": Balance,
            "Balance": EstimatedSalary,
            "Tenure": Tenure,
            "Geography": Geography,
            "Gender": Gender,
            "NumOfProducts": NumOfProducts,
            "IsActiveMember": IsActiveMember
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post("http://localhost:8000/churn/prediction", headers=headers, data=json.dumps(data))
        
        if response.json()["prediction"] > 0:
            st.error("Customer will leave.")
        else:
            st.success("Customer won't leave.")

