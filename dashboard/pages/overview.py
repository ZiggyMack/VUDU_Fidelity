"""
Overview Page - Survey Status Dashboard
"""
import streamlit as st
import sys
sys.path.insert(0, str(__file__).rsplit('pages', 1)[0])
from config import PATHS, SETTINGS
from utils import load_status, get_survey_files, load_survey_result, calculate_aggregate_metrics


def render():
    """Render the overview dashboard page"""
    st.title("📊 Overview")
    st.markdown("*Human Validation Survey Status*")
    st.markdown("---")

    # Load status
    status = load_status()

    if not status:
        st.warning("No VUDU_STATUS.json found. Dashboard is starting fresh.")
        status = {
            'project': 'VUDU Fidelity',
            'version': '0.1.0',
            'surveys': {'active': [], 'completed': [], 'draft': []},
            'metrics': {'total_responses': 0, 'active_raters': 0, 'avg_completion_time': None}
        }

    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Active Surveys",
            len(status.get('surveys', {}).get('active', [])),
            help="Currently running surveys"
        )

    with col2:
        st.metric(
            "Completed Surveys",
            len(status.get('surveys', {}).get('completed', [])),
            help="Finished surveys with results"
        )

    with col3:
        total_responses = status.get('metrics', {}).get('total_responses', 0)
        st.metric(
            "Total Responses",
            total_responses,
            help="All survey responses collected"
        )

    with col4:
        avg_time = status.get('metrics', {}).get('avg_completion_time')
        st.metric(
            "Avg Completion Time",
            f"{avg_time:.1f} min" if avg_time else "N/A",
            help="Average time to complete a survey"
        )

    st.markdown("---")

    # Current surveys section
    st.subheader("🎯 Current Focus: EXP3 Human Validation")

    st.info("""
    **Active Experiment:** EXP3 - Human Validation for Nyquist White Paper

    This survey tests whether human raters can distinguish AI persona outputs
    (T3 Ziggy) from baseline responses. Results feed into the Nyquist Consciousness
    research framework.

    **Live Survey:** [hoo-du-vu-doo.streamlit.app](https://hoo-du-vu-doo.streamlit.app/)
    """)

    # Quick links
    st.markdown("---")
    st.subheader("🔗 Quick Links")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Survey Links**
        - [Take the Survey](https://hoo-du-vu-doo.streamlit.app/)
        - [View Results](📈 Results page)
        """)

    with col2:
        st.markdown("""
        **Documentation**
        - [Rater Instructions](../RATER_INSTRUCTIONS.md)
        - [Quick Reference](../QUICK_REFERENCE.md)
        """)

    with col3:
        st.markdown("""
        **Pan Handlers**
        - [The Matrix](🔗 The Matrix page)
        - [Nyquist Dashboard](localhost:8503)
        """)
