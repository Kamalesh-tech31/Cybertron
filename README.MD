# 🛡 Cybertron

Cybertron is an AI-powered SMS Spam & Fraud Detection System built using Machine Learning, NLP, TF-IDF Vectorization, and Streamlit.

The project analyzes SMS messages in real time and classifies them as:

- ✅ Safe Message (Ham)
- 🚨 Spam / Fraudulent Message

Cybertron features a modern cybersecurity-inspired AI dashboard with a black-core hacker-style UI and emerald neon glow aesthetics.

---

# 🚀 Features

- Real-time SMS spam detection
- Machine Learning classification
- NLP preprocessing pipeline
- TF-IDF vectorization
- Confidence score analysis
- Threat keyword extraction
- Responsive AI dashboard
- Cybersecurity-inspired UI
- Streamlit frontend
- Modular architecture
- Model serialization using Joblib

---

# 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLP
- NLTK
- Pandas
- NumPy
- TF-IDF Vectorizer
- Naive Bayes
- Joblib

---

# 📁 Project Structure

```text
Cybertron/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── spam.csv
│
├── model/
│   ├── __init__.py
│   ├── predictor.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── vectorizer.py
│   ├── model_saver.py
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── notebook/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Kamalesh-tech31/Cybertron.git
```

---

## Move into Project

```bash
cd Cybertron
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Application

```bash
streamlit run app/app.py
```

---

# 🧠 Machine Learning Pipeline

The Cybertron ML pipeline works as follows:

```text
SMS Message
   ↓
Text Preprocessing
   ↓
Tokenization & Cleaning
   ↓
TF-IDF Vectorization
   ↓
Machine Learning Classification
   ↓
Spam / Safe Prediction
```

---

# 📊 Model Output

The model returns:

- Prediction Type
- Confidence Score
- Processing Time
- Detected Keywords
- Suspicious Word Count
- Believing Factors

---

# 🎨 UI Highlights

- Black-core cyberpunk theme
- Emerald neon glow effects
- AI SaaS dashboard design
- Responsive layout
- Hacker-style interface
- Unified threat analysis console

---

# 🔮 Future Improvements

- Transformer-based NLP models
- BERT integration
- Real-time phishing detection
- Multi-language spam detection
- Explainable AI insights
- Email spam filtering
- URL threat analysis

---

# 👨‍💻 Author

Kamalesh

---

# 📜 License

This project is licensed for educational and portfolio purposes.