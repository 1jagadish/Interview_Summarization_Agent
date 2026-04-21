import streamlit as st
import requests
from utils import load_transcripts

# ===== BACKEND URL =====
API_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")

# ===== DARK UI =====
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.card {
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.summary {
    background-color: #1f2937;
    color: white;
}
.strength {
    background-color: #064e3b;
    color: #d1fae5;
}
.weakness {
    background-color: #78350f;
    color: #fde68a;
}
.recommend {
    font-size: 22px;
    font-weight: bold;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
st.sidebar.title("📁 Repository")

transcripts = load_transcripts()

if not transcripts:
    st.sidebar.warning("No transcripts found in data/transcripts/")
    st.stop()

selected = st.sidebar.selectbox(
    "Select a sample transcript:",
    list(transcripts.keys())
)

transcript = transcripts[selected]

# ===== EXTRACT INFO =====
lines = transcript.split("\n")
candidate = lines[0].replace("Candidate:", "").strip() if len(lines) > 0 else "Unknown"
role = lines[1].replace("Role:", "").strip() if len(lines) > 1 else "Unknown"

# ===== HEADER =====
st.markdown("""
<h1 style='text-align:center; color:#00E5A8;'>Interview Summarization Agent</h1>
<p style='text-align:center; color:gray;'>AI-powered candidate analysis</p>
""", unsafe_allow_html=True)

# ===== LAYOUT =====
col1, col2 = st.columns(2)

# ===== LEFT SIDE =====
with col1:
    st.subheader("📄 Raw Transcript")

    st.markdown(f"""
    **Candidate:** {candidate}  
    **Role:** {role}
    """)

    st.text_area("Transcript", transcript, height=400)

# ===== RIGHT SIDE =====
with col2:
    st.subheader("🤖 Agent Output")

    if "result" not in st.session_state:
        st.session_state.result = None

    if st.button("✨ Analyze Candidate"):
        try:
            response = requests.post(
                f"{API_URL}/analyze",
                json={
                    "candidate": candidate,
                    "role": role,
                    "transcript": transcript
                }
            )

            if response.status_code == 200:
                st.session_state.result = response.json()
            else:
                st.error("Backend error. Check server.")
        except:
            st.error("Cannot connect to backend. Make sure it is running.")

    # ===== DISPLAY RESULT =====
    if st.session_state.result:
        result = st.session_state.result

        st.markdown(f"""
        <div class='card recommend'>
        🎯 Recommendation: {result['Recommendation']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📄 Executive Summary")
        st.markdown(
            f"<div class='card summary'>{result['Summary']}</div>",
            unsafe_allow_html=True
        )

        st.markdown("### ✅ Key Strengths")
        st.markdown(
            f"<div class='card strength'>{result['Strengths']}</div>",
            unsafe_allow_html=True
        )

        st.markdown("### ⚠️ Areas for Improvement")
        st.markdown(
            f"<div class='card weakness'>{result['Weaknesses']}</div>",
            unsafe_allow_html=True
        )

# ===== REPORT SECTION =====
st.markdown("---")
st.subheader("📊 Reporting")

if st.button("📥 View Saved Results"):
    try:
        res = requests.get(f"{API_URL}/results")
        st.write(res.json())
    except:
        st.error("Cannot fetch results from backend.")