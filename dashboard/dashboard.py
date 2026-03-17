import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Fake News Detector", layout="wide")

# Custom UI
st.markdown("""
<style>
.main {background-color:#f5f7fb;}
.stButton>button {
background-color:#4CAF50;
color:white;
font-size:18px;
border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI Fake News Detection System")
st.write("Real-Time News Credibility Analyzer")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:

    st.subheader("Enter News Article")
    news_input = st.text_area("Paste news here", height=200)

    if st.button("Analyze News"):

        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"text": news_input}
        )

        result = response.json()

        prediction = result["prediction"]
        score = result["credibility_score"]

        st.subheader("Result")

        if prediction == "FAKE":
            st.error("⚠️ Fake News Detected")
        else:
            st.success("✅ Real News")

        st.metric("Credibility Score", str(score) + "%")
        st.progress(score/100)

with col2:

    st.subheader("Analytics")

    df = pd.DataFrame({
        "Type": ["Fake", "Real"],
        "Count": [45, 55]
    })

    fig = px.pie(df, values="Count", names="Type", hole=0.5)
    st.plotly_chart(fig)

st.markdown("---")
st.write("AI-based Fake News Detection using NLP & ML")