import streamlit as st
import streamlit.components.v1 as components
import os

# ══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Dashboard — Semactic · Equans",
    page_icon="📊",
    layout="wide",
)

# ══════════════════════════════════════════════════════════════
# EMBED ORIGINAL DASHBOARD HTML
# ══════════════════════════════════════════════════════════════
# Hide Streamlit chrome for a clean embed
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stAppViewBlockContainer"] {padding: 0 !important;}
</style>
""", unsafe_allow_html=True)

# Load and render the original dashboard
html_path = os.path.join(os.path.dirname(__file__), "dashboard.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=7000, scrolling=True)
