import streamlit as st
import requests
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🛡️",
    layout="centered"
)

API_URL = "http://localhost:8000/predict"

# ---------------- HEADER ----------------
st.markdown("""
<style>
.big-title {
    font-size: 38px;
    font-weight: 700;
    color: #1f4fbf;
}
.sub-text {
    font-size: 16px;
    color: #6c757d;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f8f9fa;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🛡️ Insurance Premium Category Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">AI-powered insurance risk & premium classification</div>', unsafe_allow_html=True)

st.divider()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 About the App")
    st.write("""
    This application predicts your **insurance premium category**
    using a machine learning model trained on lifestyle,
    income, and demographic factors.
    """)

    st.info("💡 Tip: Accurate inputs lead to better predictions")

    st.header("⚙️ API Status")
    st.code(API_URL)

# ---------------- FORM ----------------
with st.form("insurance_form"):
    st.subheader("📋 Enter Personal Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=1, max_value=119, value=30)
        weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, value=65.0)
        smoker = st.selectbox("🚬 Smoker", options=[True, False])

    with col2:
        height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.7)
        income_lpa = st.number_input("💰 Annual Income (LPA)", min_value=0.1, value=10.0)
        occupation = st.selectbox(
            "💼 Occupation",
            [
                'retired',
                'freelancer',
                'student',
                'government_job',
                'business_owner',
                'unemployed',
                'private_job'
            ]
        )

    city = st.text_input("🏙️ City", value="Mumbai")

    submit = st.form_submit_button("🔍 Predict Premium Category")

# ---------------- API CALL ----------------
if submit:
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    with st.spinner("🔄 Analyzing risk profile..."):
        try:
            response = requests.post(API_URL, json=input_data, timeout=10)
            result = response.json()

            if response.status_code == 200 and "response" in result:
                prediction = result["response"]

                st.success("✅ Prediction Completed Successfully")

                # ---------------- METRICS ----------------
                col1, col2 = st.columns(2)
                col1.metric(
                    label="📌 Premium Category",
                    value=prediction["predicted_category"]
                )
                col2.metric(
                    label="🎯 Model Confidence",
                    value=f"{prediction['confidence'] * 100:.2f}%"
                )

                # ---------------- PROBABILITIES ----------------
                st.subheader("📊 Class Probability Distribution")

                prob_df = pd.DataFrame(
                    prediction["class_probabilities"].items(),
                    columns=["Category", "Probability"]
                )

                st.bar_chart(prob_df.set_index("Category"))

                # ---------------- RAW JSON ----------------
                with st.expander("🔎 View Raw API Response"):
                    st.json(result)

            else:
                st.error(f"❌ API Error: {response.status_code}")
                st.json(result)

        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to FastAPI server. Is it running?")
        except Exception as e:
            st.error("⚠️ Unexpected error occurred")
            st.exception(e)

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 | Insurance ML Predictor | Built with FastAPI + Streamlit 🚀")
