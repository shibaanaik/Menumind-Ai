# app.py
import streamlit as st

st.set_page_config(page_title="MenuMind AI", layout="wide")
st.title("🍽️ Welcome to MenuMind AI")

st.markdown("""
This is a smart menu intelligence system that recommends dishes based on:
- Regional food trends 🍛
- Customer cravings 😋
""")

st.markdown("Use the sidebar to navigate between pages ➡️")

# Add footer
st.markdown(
    """
    <hr style="margin-top: 2em;">
    <div style="text-align: center; color: gray;">
        Made by Shibaa
    </div>
    """,
    unsafe_allow_html=True
)
