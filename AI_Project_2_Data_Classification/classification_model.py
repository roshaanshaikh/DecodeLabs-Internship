# DecodeLabs AI Project 2
# Data Classification Using AI
# Iris Dataset Classification using K-Nearest Neighbors

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN Model
model = KNeighborsClassifier(n_neighbors=5)

# Training
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)

print("AI Data Classification Model")
print("----------------------------")
print("Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Test New Sample
sample = [[5.1, 3.5, 1.4, 0.2]]
sample = scaler.transform(sample)

result = model.predict(sample)

print("Prediction Class:", iris.target_names[result][0])
