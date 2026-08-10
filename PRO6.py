# Program no 6: Implement Naïve Bayes Classifier, Compute Accuracy and Visualize Performance
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.30,
    random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", round(accuracy * 100, 2), "%")

ConfusionMatrixDisplay.from_predictions(y_test, prediction)
plt.title("Naive Bayes Confusion Matrix")
plt.show()
