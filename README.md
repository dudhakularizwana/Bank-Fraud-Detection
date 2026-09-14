# 🏦 Bank Fraud Detection System

## 📌 Project Overview

The **Bank Fraud Detection System** is a Machine Learning project designed to identify whether a bank transaction is **fraudulent or legitimate**.

The system uses transaction details such as transaction type, transaction amount, sender balance, and receiver balance to predict possible fraudulent transactions.

The project includes a **Machine Learning model**, a **Streamlit web application**, and a **GitHub repository** for project management and sharing.

---

## 🎯 Objective

The main objective of this project is to:

- Detect fraudulent bank transactions.
- Use Machine Learning to classify transactions as Fraud or Not Fraud.
- Compare different Machine Learning models.
- Build an easy-to-use web interface using Streamlit.
- Deploy the application so it can be accessed online.

---

## 🛠️ Technologies Used

- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 💾 Joblib
- 📈 Matplotlib
- 🌐 Streamlit
- 🐙 Git & GitHub

---

## 🤖 Machine Learning Models

The project uses Machine Learning algorithms for fraud detection.

### 1. Logistic Regression

Logistic Regression is used as a classification algorithm to predict whether a transaction is fraudulent or legitimate.

### 2. Random Forest Classifier

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to improve prediction performance.

The Random Forest model provided better overall fraud detection performance compared with the Logistic Regression model.

---

## 📂 Dataset

The project uses a **Bank Fraud Detection dataset** containing transaction information.

Important features include:

- `step`
- `type`
- `amount`
- `nameOrig`
- `oldbalanceOrg`
- `newbalanceOrig`
- `nameDest`
- `oldbalanceDest`
- `newbalanceDest`
- `isFraud`

### Target Variable

`isFraud`

- `0` → Not Fraud
- `1` → Fraud

> ⚠️ The original dataset is not uploaded to this public GitHub repository because it is a large dataset. It is excluded using `.gitignore`.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Encoding
   ↓
Train-Test Split
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Web Application
   ↓
Fraud / Not Fraud Prediction

---

## 👩‍💻 Author

**Rizwana Dudekula**

B.Tech – Computer Science and Engineering (Artificial Intelligence)

---

## ⭐ Conclusion

The **Bank Fraud Detection System** demonstrates how Machine Learning can be used to identify potentially fraudulent bank transactions.

The project includes **data preprocessing, feature encoding, model training, model evaluation, and prediction**.

The trained Machine Learning model is integrated with a **Streamlit web application**, allowing users to enter transaction details and get a fraud detection prediction.

This project provided practical experience in **Python, Machine Learning, Scikit-learn, Streamlit, Git, GitHub, and deployment**.

---

## ⭐ Thank You

Thank you for visiting my project! 😊

If you find this project useful, please consider giving the repository a ⭐ **Star** on GitHub.
