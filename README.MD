🛡 Cybertron

An AI-powered SMS spam classification system built using Machine Learning and Natural Language Processing (NLP).

---

🚀 Features

- Spam & Ham SMS Classification
- NLP Text Preprocessing
- TF-IDF Vectorization
- Suspicious Keyword Detection
- Confidence Score Prediction
- Real-time SMS Analysis
- Intelligent Spam Pattern Recognition

---

🧠 Tech Stack

- Python
- Scikit-learn
- Pandas
- NLTK
- NumPy
- TF-IDF Vectorizer
- Streamlit

---

📂 Project Structure

Cybertron/
│
├── app/
│
├── dataset/
│   └── spam.csv
│
├── model/
│   ├── predictor.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── vectorizer.py
│   ├── model_saver.py
│   ├── spam_model.pkl
│   ├── vectorizer.pkl
│
├── notebook/
│
├── venv/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore

---

⚙ Installation

Clone the repository:

git clone <your-repository-link>

Move into the project folder:

cd Cybertron

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py