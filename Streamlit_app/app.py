import streamlit as st
import pickle
import numpy as np
import os

# Load model

model_path = os.path.join(os.path.dirname(__file__), 'RF_Model.pkl')
model = pickle.load(open(model_path, 'rb'))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction System")

st.markdown("Fill the details below:")

# Numeric inputs
tenure = st.number_input("Tenure", min_value=0)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

# Dropdowns
gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Partner", ["No", "Yes"])
Dependents = st.selectbox("Dependents", ["No", "Yes"])
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("Online Security", ["No", "Yes"])
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

tenure_group = st.number_input("Tenure Group", min_value=0)

# Encoding (IMPORTANT)
def encode_binary(val):
    return 1 if val == "Yes" else 0

def encode_gender(val):
    return 1 if val == "Male" else 0

def encode_internet(val):
    return {"DSL": 0, "Fiber optic": 1, "No": 2}[val]

def encode_contract(val):
    return {"Month-to-month": 0, "One year": 1, "Two year": 2}[val]

def encode_payment(val):
    return {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer": 2,
        "Credit card": 3
    }[val]

def encode_multiple(val):
    return {"No": 0, "Yes": 1, "No phone service": 2}[val]

# Predict button
if st.button("Predict"):

    features = [
        tenure,
        MonthlyCharges,
        TotalCharges,
        encode_gender(gender),
        encode_binary(SeniorCitizen),
        encode_binary(Partner),
        encode_binary(Dependents),
        encode_binary(PhoneService),
        encode_multiple(MultipleLines),
        encode_internet(InternetService),
        encode_binary(OnlineSecurity),
        encode_binary(OnlineBackup),
        encode_binary(DeviceProtection),
        encode_binary(TechSupport),
        encode_binary(StreamingTV),
        encode_binary(StreamingMovies),
        encode_contract(Contract),
        encode_binary(PaperlessBilling),
        encode_payment(PaymentMethod),
        tenure_group
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("⚠️ Customer Will Churn")
    else:
        st.success("✅ Customer Will Stay")