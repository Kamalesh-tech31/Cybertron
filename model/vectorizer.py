from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    vectorizer = TfidfVectorizer() #Term frequency-Inverse document frequency (TF-IDF) vectorizer to convert text data into numerical features.
    return vectorizer