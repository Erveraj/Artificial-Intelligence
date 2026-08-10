#Program No 11: Extract Term Frequency Using a Bag of Words Model
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "AI is intelligent",
    "AI is useful",
    "Python is useful for AI"
]

vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(bow.toarray())

print("\nTotal Term Frequency:")
frequencies = bow.toarray().sum(axis=0)
for word, frequency in zip(
    vectorizer.get_feature_names_out(), frequencies
):
    print(word, ":", frequency)
