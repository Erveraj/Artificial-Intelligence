#Program No: 12 Predict the Category of a Given Piece of Text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "team won the cricket match",
    "player scored a goal",
    "new software uses artificial intelligence",
    "python is a programming language"
]

labels = ["Sports", "Sports", "Technology", "Technology"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

new_text = ["AI software is written using python"]
new_X = vectorizer.transform(new_text)

prediction = model.predict(new_X)

print("Text:", new_text[0])
print("Predicted Category:", prediction[0])
