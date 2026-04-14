import streamlit as st
import pickle
import numpy as np
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'RF_Model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Page config
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center;'>📊 Customer Churn Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown("""
This system predicts whether a customer will **stay or leave (churn)** based on their details.
""")

# Fill the details below:


# ------------------ INPUT SECTION ------------------

# Tenure
tenure = st.number_input(
    "🕒 Tenure",
    min_value=0,
    help="How many months the customer has used the service.\nExample: 12 means 1 year."
)

# Monthly Charges
MonthlyCharges = st.number_input(
    "💰 Monthly Charges",
    min_value=0.0,
    help="Amount the customer pays every month.\nExample: ₹500 per month."
)

# Total Charges
TotalCharges = st.number_input(
    "💵 Total Charges",
    min_value=0.0,
    help="Total amount paid by the customer till now.\nExample: ₹10,000 total."
)

# Basic info
gender = st.selectbox("👤 Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("👴 Senior Citizen (Age 60+?)", ["No", "Yes"])

# Family info
Partner = st.selectbox("💑 Has Partner?", ["No", "Yes"])
Dependents = st.selectbox("👶 Has Dependents?", ["No", "Yes"])

# Services
PhoneService = st.selectbox("📞 Phone Service?", ["No", "Yes"])
MultipleLines = st.selectbox("📱 Multiple Phone Lines?", ["No", "Yes", "No phone service"])

InternetService = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("🔒 Online Security?", ["No", "Yes"])
OnlineBackup = st.selectbox("💾 Online Backup?", ["No", "Yes"])
DeviceProtection = st.selectbox("🛡 Device Protection?", ["No", "Yes"])
TechSupport = st.selectbox("🧑‍💻 Tech Support?", ["No", "Yes"])

StreamingTV = st.selectbox("📺 Streaming TV?", ["No", "Yes"])
StreamingMovies = st.selectbox("🎬 Streaming Movies?", ["No", "Yes"])

# Billing
Contract = st.selectbox("📄 Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("📧 Paperless Billing?", ["No", "Yes"])

PaymentMethod = st.selectbox(
    "💳 Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

tenure_group = st.number_input(
    "📊 Tenure Group",
    min_value=0,
    help="You can enter same as tenure or grouped value"
)

# ------------------ ENCODING ------------------

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

# ------------------ PREDICTION ------------------

st.markdown("---")

if st.button("🔍 Predict Customer Status"):

    # Validation check
    if tenure == 0 or MonthlyCharges == 0 or TotalCharges == 0:
        st.warning("⚠️ Please fill all important fields before prediction!")
    else:
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

        st.markdown("## 📢 Result")

        if prediction[0] == 1:
            st.error("⚠️ This customer is likely to LEAVE (Churn)")
        else:
            st.success("✅ This customer is likely to STAY")
