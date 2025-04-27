# Step 1: Install & Import Libraries
import nltk
nltk.data.path.append("/home/codeany/nltk_data")

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Step 2: Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Step 3: Sample Document
document = """Natural Language Processing (NLP) is a field of artificial intelligence that enables computers to understand, interpret, and generate human language. It involves applying algorithms to identify and extract the natural language rules such that the unstructured language data is converted into a form that computers can understand."""

# Step 4: Preprocessing

# REGEX Tokenization (bypassing punkt)
tokens = re.findall(r'\b\w+\b', document)
print("Tokens:", tokens)

# POS Tagging
pos_tags = pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

# Stop Words Removal
stop_words = set(stopwords.words('english'))
tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
print("\nTokens without Stopwords:", tokens_without_stopwords)

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens_without_stopwords]
print("\nStemmed Tokens:", stemmed_tokens)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens_without_stopwords]
print("\nLemmatized Tokens:", lemmatized_tokens)

# Step 5: TF-IDF Representation

# Convert back to text after processing
processed_text = ' '.join(lemmatized_tokens)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([processed_text])

# Display TF-IDF values
feature_names = vectorizer.get_feature_names_out()
print("\nTF-IDF Scores:")
for col in range(tfidf_matrix.shape[1]):
    print(f"{feature_names[col]}: {tfidf_matrix[0, col]:.4f}")
