import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Text preprocessing function to clean the text data by converting to lowercase, removing punctuation, and removing stop words.
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)