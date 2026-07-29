import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("../dataset/loan_data.csv")

# Convert categorical values
data = pd.get_dummies(data, drop_first=True)

# Features and target
X = data.drop("Loan_Status_Y", axis=1)
y = data["Loan_Status_Y"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "model.pkl")

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Model trained successfully!")

print("Accuracy :", accuracy)
