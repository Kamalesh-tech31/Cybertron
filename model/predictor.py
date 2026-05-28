import time

from model.model_saver import load_model
from model.preprocessing import clean_text

# Load saved model
model = load_model("model/spam_model.pkl")

# Load saved vectorizer
vectorizer = load_model("model/vectorizer.pkl")


SPAM_WORDS = [
    "free",
    "winner",
    "offer",
    "click",
    "prize",
    "cash",
    "urgent",
    "claim",
    "money",
    "buy"
]

SAFE_WORDS = [
    "meeting",
    "project",
    "family",
    "schedule",
    "discussion",
    "class",
    "assignment",
    "tomorrow",
    "office"
]

def predict_message(message):

    start_time = time.time()

    # Clean message
    cleaned_message = clean_text(message)

     # Extract keywords
    keywords = cleaned_message.split()


    # Convert into vector
    transformed_message = vectorizer.transform([cleaned_message])

    # Predict
    prediction = model.predict(transformed_message)

     # Predict probabilities
    probabilities = model.predict_proba(transformed_message)[0]

    ham_probability = probabilities[0]
    spam_probability = probabilities[1]

    end_time = time.time()

    processing_time = round(end_time - start_time, 4)

    # Spam prediction
    if prediction == 1:

        suspicious_words = [
            word for word in keywords
            if word in SPAM_WORDS
        ]

        return {
            "prediction": "Spam",
            "confidence": round(spam_probability * 100, 2),
            "processing_time": f"{processing_time} sec",
            "detected_keywords": keywords,
            "suspicious_words": suspicious_words
        }
    
     # Not spam prediction
    else:

        believing_factors = [
            word for word in keywords
            if word in SAFE_WORDS
        ]

        return {
            "prediction": "Not Spam",
            "confidence": round(ham_probability * 100, 2),
            "processing_time": f"{processing_time} sec",
            "detected_keywords": keywords,
            "believing_factors": believing_factors
        }