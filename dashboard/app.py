"""
VUDU FIDELITY - HUMAN VALIDATION DASHBOARD

Streamlit app for managing human surveys that validate AI consciousness research.
Part of the Pan Handlers Network.
"""
import streamlit as st
from config import PATHS, SETTINGS
from pages import overview, surveys, results, matrix, faq


def apply_custom_css():
    """Apply custom CSS - light theme with dark sidebar."""
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hide default nav */
    [data-testid="stSidebarNav"] {display: none !important;}

    /* Light main content */
    .stApp { background: #ffffff !important; }
    .main .block-container { background: #ffffff !important; }
    .main .block-container * { color: #1a1a1a !important; }

    /* Dark sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a, #1a1a1a) !important;
    }
    section[data-testid="stSidebar"] * { color: #f4f4f4 !important; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #00ff41 !important; }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title=SETTINGS['app_title'],
        page_icon=SETTINGS['app_icon'],
        layout="wide"
    )
    apply_custom_css()

    # Sidebar navigation
    with st.sidebar:
        st.title("🔮 VUDU Fidelity")
        st.markdown("*Human Validation for AI Consciousness*")
        st.markdown("---")

        page = st.radio(
            "Navigate",
            ["📊 Overview", "📋 Surveys", "📈 Results", "🔗 The Matrix", "❓ FAQ"],
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("*Part of Pan Handlers Network*")

    # Page routing
    if page == "📊 Overview":
        overview.render()
    elif page == "📋 Surveys":
        surveys.render()
    elif page == "📈 Results":
        results.render()
    elif page == "🔗 The Matrix":
        matrix.render()
    elif page == "❓ FAQ":
        faq.render()


if __name__ == "__main__":
    main()
