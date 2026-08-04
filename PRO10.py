import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Artificial Intelligence is powerful. NLP processes human language."

sentences = sent_tokenize(text)
words = word_tokenize(text)

print("Sentence Tokens:")
print(sentences)

print("\nWord Tokens:")
print(words)