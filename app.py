import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("fraud_model.pkl")
encoder = joblib.load("encoder.pkl")

# Page configuration
st.set_page_config(
    page_title="Bank Fraud Detection",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Bank Fraud Detection System")

st.write(
    "Enter the transaction details below to check whether "
    "the transaction is fraudulent."
)

st.divider()

# Transaction details
st.subheader("💳 Transaction Details")

step = st.number_input(
    "Step",
    min_value=0,
    value=200
)

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "CASH_OUT", "CASH_IN", "TRANSFER", "DEBIT"]
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=10000.0
)

st.subheader("👤 Sender Information")

oldbalanceOrg = st.number_input(
    "Sender Old Balance",
    min_value=0.0,
    value=10000.0
)

newbalanceOrig = st.number_input(
    "Sender New Balance",
    min_value=0.0,
    value=0.0
)

st.subheader("🏦 Receiver Information")

oldbalanceDest = st.number_input(
    "Receiver Old Balance",
    min_value=0.0,
    value=5000.0
)

newbalanceDest = st.number_input(
    "Receiver New Balance",
    min_value=0.0,
    value=15000.0
)

st.divider()

# Prediction button
if st.button("🔍 Check Transaction", use_container_width=True):

    # Convert transaction type into number
    type_encoded = encoder.transform([transaction_type])[0]

    # Create input data
    new_transaction = pd.DataFrame([[
        step,
        type_encoded,
        amount,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest
    ]], columns=[
        "step",
        "type",
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest"
    ])

    # Prediction
    prediction = model.predict(new_transaction)

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.error("🚨 FRAUD TRANSACTION DETECTED!")
        st.warning(
            "This transaction has been classified as potentially fraudulent."
        )
    else:
        st.success("✅ TRANSACTION IS NOT FRAUD")
        st.info(
            "This transaction has been classified as a normal transaction."
        )