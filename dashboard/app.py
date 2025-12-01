"""
VUDU FIDELITY - HUMAN VALIDATION DASHBOARD

Streamlit app for managing human surveys that validate AI consciousness research.
Part of the Pan Handlers Network.
"""
import streamlit as st
from config import PATHS, SETTINGS
from pages import overview, surveys, results, matrix, faq


def apply_custom_css(is_matrix_page=False):
    """Apply custom CSS - light theme with dark sidebar (unless Matrix page)."""

    # Base CSS that always applies
    base_css = """
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hide default nav */
    [data-testid="stSidebarNav"] {display: none !important;}

    /* Dark sidebar - always */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a, #1a1a1a) !important;
    }
    section[data-testid="stSidebar"] * { color: #f4f4f4 !important; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #00ff41 !important; }

    /* Matrix button in sidebar - prominent green styling */
    section[data-testid="stSidebar"] .stButton > button {
        background-color: #0d0d0d !important;
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
    }
    section[data-testid="stSidebar"] .stButton > button p,
    section[data-testid="stSidebar"] .stButton > button span,
    section[data-testid="stSidebar"] .stButton > button div {
        color: #00ff41 !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #004d1a !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(0,255,65,0.4);
    }
    section[data-testid="stSidebar"] .stButton > button:hover p,
    section[data-testid="stSidebar"] .stButton > button:hover span,
    section[data-testid="stSidebar"] .stButton > button:hover div {
        color: #ffffff !important;
    }
    """

    # Light theme CSS - only for non-Matrix pages
    light_theme_css = """
    /* Light main content */
    .stApp { background: #ffffff !important; }
    .main .block-container { background: #ffffff !important; }
    .main .block-container * { color: #1a1a1a !important; }
    """ if not is_matrix_page else ""

    st.markdown(f"""
    <style>
    {base_css}
    {light_theme_css}
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title=SETTINGS['app_title'],
        page_icon=SETTINGS['app_icon'],
        layout="wide"
    )

    # Initialize page in session state
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "📊 Overview"

    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🔮 VUDU Fidelity")
        st.markdown("*Human Validation for AI Consciousness*")

        st.markdown("Turn the page:")

        # Navigation radio buttons
        page = st.radio(
            "Navigate",
            ["📊 Overview", "📋 Surveys", "📈 Results", "❓ FAQ"],
            label_visibility="collapsed",
            key="nav_radio"
        )

        st.markdown("---")

        # Matrix button - standalone and prominent
        if st.button("🟢 Enter The Matrix", use_container_width=True):
            st.session_state['current_page'] = "🔗 The Matrix"
            page = "🔗 The Matrix"

    # Determine actual page (Matrix button overrides radio)
    if st.session_state.get('current_page') == "🔗 The Matrix" and page != "🔗 The Matrix":
        # User clicked a radio option, exit Matrix
        st.session_state['current_page'] = page
    elif page != st.session_state.get('current_page') and st.session_state.get('current_page') != "🔗 The Matrix":
        st.session_state['current_page'] = page

    current_page = st.session_state['current_page']

    # Apply CSS - skip light theme for Matrix page
    is_matrix = (current_page == "🔗 The Matrix")
    apply_custom_css(is_matrix_page=is_matrix)

    # Page routing
    if current_page == "📊 Overview":
        overview.render()
    elif current_page == "📋 Surveys":
        surveys.render()
    elif current_page == "📈 Results":
        results.render()
    elif current_page == "🔗 The Matrix":
        matrix.render()
    elif current_page == "❓ FAQ":
        faq.render()


if __name__ == "__main__":
    main()
