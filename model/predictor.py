import time

from model.model_saver import load_model
from model.preprocessing import clean_text

# Load trained model
model = load_model("model/spam_model.pkl")

# Load vectorizer
vectorizer = load_model("model/vectorizer.pkl")


def predict_message(message):

    start_time = time.time()

    # Clean text
    cleaned_message = clean_text(message)

    # Extract keywords from cleaned message
    keywords = cleaned_message.split()

    # Convert text into vector
    transformed_message = vectorizer.transform([cleaned_message])

    # Predict class
    prediction = model.predict(transformed_message)[0]

    # Prediction probabilities
    probabilities = model.predict_proba(transformed_message)[0]

    ham_probability = probabilities[0]
    spam_probability = probabilities[1]

    # Confidence calculation
    if prediction == 1:
        confidence = spam_probability * 100
        prediction_label = "Spam"
    else:
        confidence = ham_probability * 100
        prediction_label = "Not Spam"

    end_time = time.time()

    processing_time = round(end_time - start_time, 4)

    return {

        "prediction": prediction_label,

        "confidence": round(confidence, 2),

        "spam_probability": round(spam_probability * 100, 2),

        "ham_probability": round(ham_probability * 100, 2),

        "processing_time": f"{processing_time} sec",

        "detected_keywords": keywords
    }