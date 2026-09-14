import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load dataset
df = pd.read_csv("Bank Fraud Detection.csv")

print("Dataset loaded successfully!")
print(df.head())

# 2. Check dataset information
print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# 3. Convert transaction type into numbers
encoder = LabelEncoder()
df["type"] = encoder.fit_transform(df["type"])

# 4. Select input features
X = df[["step", "type", "amount", "oldbalanceOrg",
        "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]]

# 5. Target
y = df["isFraud"]

# 6. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 8. Train model
model.fit(X_train, y_train)

# 9. Prediction
y_pred = model.predict(X_test)

# 10. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

# 11. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# 12. Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 13. Visualization
plt.figure(figsize=(6, 4))
plt.imshow(cm)
plt.title("Fraud Detection Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()

plt.xticks([0, 1], ["Not Fraud", "Fraud"])
plt.yticks([0, 1], ["Not Fraud", "Fraud"])

plt.show()

# 14. Feature importance
importance = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.bar(X.columns, importance)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 15. Test a new transaction
print("\n--- New Transaction Test ---")

amount = float(input("Enter amount: "))

new_transaction = [[
    200,
    encoder.transform(["PAYMENT"])[0],
    amount,
    10000,
    10000 - amount,
    5000,
    5000
]]

prediction = model.predict(new_transaction)

if prediction[0] == 1:
    print("⚠️ FRAUD TRANSACTION DETECTED!")
else:
    print("✅ TRANSACTION IS NOT FRAUD")
import joblib

joblib.dump(model, "fraud_model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("\nModel saved successfully!")