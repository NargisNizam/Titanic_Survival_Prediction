import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load Dataset
df = pd.read_csv("titanic_dataset/train_and_test2.csv")

# Select useful features
features = [
    "Passengerid",
    "Age",
    "Fare",
    "Sex",
    "sibsp",
    "Parch",
    "Pclass",
    "Embarked"
]

target = "2urvived"


# Prepare data
X = df[features].copy()
y = df[target]


# Fill missing values
X["Age"] = X["Age"].fillna(X["Age"].median())
X["Fare"] = X["Fare"].fillna(X["Fare"].median())
X["Embarked"] = X["Embarked"].fillna(X["Embarked"].mode()[0])


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)


print("=" * 45)
print("Titanic Survival Prediction Model")
print("=" * 45)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("=" * 45)


# Save model
joblib.dump(model, "model.pkl")

print("model.pkl saved successfully!")