"""
Surveys Page - Manage Active and Completed Surveys
"""
import streamlit as st
import sys
sys.path.insert(0, str(__file__).rsplit('pages', 1)[0])
from config import PATHS, SETTINGS
from utils import load_status


def render():
    """Render the surveys management page"""
    st.title("📋 Surveys")
    st.markdown("*Manage Human Validation Surveys*")
    st.markdown("---")

    # Load status
    status = load_status()
    surveys = status.get('surveys', {}) if status else {}

    # Tabs for different survey states
    tab1, tab2, tab3 = st.tabs(["🟢 Active", "✅ Completed", "📝 Drafts"])

    with tab1:
        st.subheader("Active Surveys")
        active = surveys.get('active', [])

        if not active:
            # Show the main EXP3 survey as active
            st.markdown("""
            <div style="background: #f0fff0; padding: 1.5rem; border-left: 4px solid #00ff41; border-radius: 4px; margin: 1rem 0;">
                <h4 style="color: #1a1a1a; margin: 0;">EXP3 - Human Validation Survey</h4>
                <p style="color: #333; margin: 0.5rem 0;">Testing AI persona (Ziggy) identity persistence through blind comparison.</p>
                <p style="color: #666; margin: 0.5rem 0;"><strong>Status:</strong> Live | <strong>Responses:</strong> Collecting</p>
                <p style="color: #333; margin: 0.5rem 0;"><a href="https://hoo-du-vu-doo.streamlit.app/" target="_blank">🔗 Take Survey</a></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for survey in active:
                st.markdown(f"""
                <div style="background: #f0fff0; padding: 1rem; border-left: 4px solid #00ff41; border-radius: 4px; margin: 0.5rem 0;">
                    <strong>{survey.get('name', 'Unnamed Survey')}</strong><br>
                    Status: {survey.get('status', 'Active')}
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Completed Surveys")
        completed = surveys.get('completed', [])

        if not completed:
            st.info("No completed surveys yet. Results will appear here once surveys are finalized.")
        else:
            for survey in completed:
                st.markdown(f"""
                <div style="background: #f0f0ff; padding: 1rem; border-left: 4px solid #2a9d8f; border-radius: 4px; margin: 0.5rem 0;">
                    <strong>{survey.get('name', 'Unnamed Survey')}</strong><br>
                    Completed: {survey.get('completed_date', 'Unknown')} |
                    Responses: {survey.get('response_count', 0)}
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        st.subheader("Draft Surveys")
        drafts = surveys.get('draft', [])

        if not drafts:
            st.info("No draft surveys. Create a new survey template to get started.")
        else:
            for survey in drafts:
                st.markdown(f"""
                <div style="background: #fff5f0; padding: 1rem; border-left: 4px solid #e76f51; border-radius: 4px; margin: 0.5rem 0;">
                    <strong>{survey.get('name', 'Unnamed Survey')}</strong><br>
                    Status: Draft
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    # Survey creation hint
    st.subheader("📝 Creating New Surveys")
    st.markdown("""
    To create a new survey:
    1. Copy and modify `app.py` with new scenarios
    2. Deploy to Streamlit Cloud or run locally
    3. Update `VUDU_STATUS.json` with survey metadata

    See [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md) for detailed instructions.
    """)
