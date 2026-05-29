import sys
import os
import time
import random
import streamlit as st

# ---------------- PATH FIX ---------------- #

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from model.predictor import predict_message

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Cybertron",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #000000;
    color: #E5FFF5;
}

/* Main Background */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(16,185,129,0.15), transparent 25%),
        radial-gradient(circle at bottom right, rgba(16,185,129,0.08), transparent 25%),
        #000000;
}

/* Remove Streamlit padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #020202 0%,
        #07110D 70%
    );
    border-right: 1px solid rgba(16,185,129,0.12);
}

/* Sidebar cards */
.sidebar-card {
    background: rgba(0,0,0,0.55);
    border: 1px solid rgba(16,185,129,0.18);
    border-radius: 18px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 0 18px rgba(16,185,129,0.08);
}

/* Main Hero */
.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    color: #ECFDF5;
    text-align: center;
    text-shadow:
        0 0 10px rgba(16,185,129,0.6),
        0 0 25px rgba(16,185,129,0.4),
        0 0 45px rgba(16,185,129,0.2);
}

.hero-sub {
    text-align: center;
    color: #6EE7B7;
    font-size: 1.5rem;
    margin-top: 0px;
    margin-bottom: 2rem;
}

/* Main dashboard card */
.cyber-card {
    background: rgba(3, 7, 6, 0.92);
    border: 1px solid rgba(16,185,129,0.16);
    border-radius: 24px;
    padding: 2rem;
    box-shadow:
        0 0 20px rgba(16,185,129,0.08),
        inset 0 0 25px rgba(16,185,129,0.03);
}

/* Result cards */
.result-spam {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.28);
    border-radius: 18px;
    padding: 1.4rem;
    box-shadow: 0 0 25px rgba(239,68,68,0.18);
}

.result-safe {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.28);
    border-radius: 18px;
    padding: 1.4rem;
    box-shadow: 0 0 25px rgba(34,197,94,0.18);
}

/* Text area */
textarea {
    background: #020202 !important;
    color: #E5FFF5 !important;
    border-radius: 20px !important;
    border: 1px solid rgba(16,185,129,0.25) !important;
    font-size: 1rem !important;
    padding: 1rem !important;
}

/* Analyze button */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 18px;
    background: linear-gradient(
        90deg,
        #059669,
        #10B981,
        #34D399
    );
    color: white;
    padding: 1rem;
    font-size: 1rem;
    font-weight: 700;
    transition: 0.3s ease;
    box-shadow: 0 0 25px rgba(16,185,129,0.22);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow:
        0 0 40px rgba(16,185,129,0.35),
        0 0 80px rgba(16,185,129,0.15);
}

/* Chips */
.keyword-chip {
    display: inline-block;
    padding: 0.45rem 1rem;
    margin: 0.3rem;
    border-radius: 999px;
    border: 1px solid rgba(16,185,129,0.25);
    background: rgba(16,185,129,0.06);
    color: #D1FAE5;
    font-size: 0.85rem;
    font-weight: 500;
}

/* Metric glow */
[data-testid="metric-container"] {
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(16,185,129,0.14);
    padding: 1rem;
    border-radius: 16px;
    box-shadow: 0 0 16px rgba(16,185,129,0.06);
}

/* Footer */
.footer {
    text-align: center;
    color: #6EE7B7;
    margin-top: 2rem;
    opacity: 0.8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.markdown("""
    <div style="
        font-size:2rem;
        font-weight:800;
        color:#6EE7B7;
        margin-bottom:2rem;
        text-shadow:0 0 18px rgba(16,185,129,0.5);
    ">
    ⚡ Cybertron
    </div>
    """, unsafe_allow_html=True)

    stats = [
        ("📩 Messages Analyzed", "1000+"),
        ("🛡 Spam Blocked", "500+"),
        ("⚡ Avg Detection Speed", "0.08s"),
        ("🧠 AI Engine", "Naive Bayes")
    ]

    for title, value in stats:
        st.markdown(f"""
        <div class="sidebar-card">
            <div style="font-size:0.9rem;color:#9CA3AF;">{title}</div>
            <div style="
                font-size:2rem;
                font-weight:700;
                color:#ECFDF5;
                margin-top:8px;
            ">
                {value}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown("""
            
<div class="hero-title">
⚡Cybertron
</div>
<div class="hero-sub">
Real-Time SMS Threat Detection using Machine Learning Classification Model
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN DASHBOARD ---------------- #

st.subheader("📡 Message Analysis Console")

message = st.text_area(
    "SMS Message",
    height=220,
    placeholder="Paste suspicious SMS content here...",
    label_visibility="collapsed"
)

analyze = st.button("🔍 Analyze")

# ---------------- RESULT ---------------- #

if analyze and message.strip():

    with st.spinner("Cybertron AI analyzing message..."):
        time.sleep(1)
        result = predict_message(message)

    prediction = result["prediction"]
    confidence = result["confidence"]
    processing_time = result["processing_time"]
    keywords = result["detected_keywords"]

    st.divider()

    # RESULT BANNER

    if prediction == "Spam":

        st.markdown("""
        <div class="result-spam">
            <h2>🚨 HIGH RISK MESSAGE DETECTED</h2>
            <p>Cybertron identified suspicious spam behavior patterns.</p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-safe">
            <h2>✅ MESSAGE VERIFIED SAFE</h2>
            <p>No suspicious behavior patterns detected.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # METRICS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Prediction", prediction)

    with col2:
        st.metric("Confidence", f"{confidence}%")

    with col3:
        st.metric("Processing", processing_time)

    with col4:
        if prediction == "Spam":
            st.metric(
                "Suspicious Words",
                len(result["suspicious_words"])
            )
        else:
            st.metric(
                "Believing Factors",
                len(result["believing_factors"])
            )

    st.divider()

    # CONFIDENCE BAR

    st.subheader("⚡ Threat Confidence")

    st.progress(int(confidence))

    st.caption(f"Threat Confidence Score: {confidence}%")

    st.divider()

    # KEYWORDS

    st.subheader("🧠 Detected NLP Keywords")

    keyword_html = ""

    for word in keywords:
        keyword_html += f"""
        <span class="keyword-chip">
            {word}
        </span>
        """

    st.markdown(keyword_html, unsafe_allow_html=True)


# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">
Cybertron - AI-Powered SMS filtering system
</div>
""", unsafe_allow_html=True)