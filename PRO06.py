# Program no 6: Implement Naïve Bayes Classifier, Compute Accuracy and Visualize Performance
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


# Load Iris dataset
data = load_iris()

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.30,
    random_state=42
)

# Create Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, prediction)

# Display accuracy
print("Accuracy:", round(accuracy * 100, 2), "%")

# Display confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test, prediction)

plt.title("Naive Bayes Confusion Matrix")
plt.show()
