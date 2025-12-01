"""
Results Page - Survey Results and Analysis
"""
import streamlit as st
import json
import sys
sys.path.insert(0, str(__file__).rsplit('pages', 1)[0])
from config import PATHS, SETTINGS
from utils import get_survey_files, load_survey_result, calculate_aggregate_metrics


def render():
    """Render the results analysis page"""
    st.title("📈 Results")
    st.markdown("*Survey Results and Analysis*")
    st.markdown("---")

    # Check for results directory
    results_dir = PATHS['results_dir']

    if not results_dir.exists():
        st.info("""
        **No results directory found.**

        Survey results will appear here once raters complete surveys and
        submit their JSON files.

        **To add results:**
        1. Create a `results/` folder in the repo root
        2. Save JSON result files from completed surveys
        3. Refresh this page
        """)

        # Show sample result structure
        st.subheader("📋 Expected Result Format")
        sample = {
            "test_version": "2.0",
            "rater": {"username": "example_rater", "favorite_movie": "The Matrix"},
            "completed_at": "2025-12-01T12:00:00",
            "duration_minutes": 8.5,
            "responses": [{"scenario_id": 1, "voice_choice": "Definitely Response A", "confidence": "Very confident"}],
            "summary": {"pfi_human": 0.75, "mean_confidence": 2.5}
        }
        st.code(json.dumps(sample, indent=2), language="json")
        return

    # Load all results
    result_files = get_survey_files()

    if not result_files:
        st.info("No result files found in the results directory.")
        return

    results = []
    for f in result_files:
        try:
            results.append(load_survey_result(f))
        except Exception as e:
            st.warning(f"Could not load {f.name}: {e}")

    if not results:
        st.warning("Could not load any result files.")
        return

    # Aggregate metrics
    metrics = calculate_aggregate_metrics(results)

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Responses", metrics['total_responses'])

    with col2:
        pfi = metrics['avg_pfi']
        st.metric("Avg PFI Score", f"{pfi:.2f}" if pfi else "N/A")

    with col3:
        conf = metrics['avg_confidence']
        st.metric("Avg Confidence", f"{conf:.1f}/3" if conf else "N/A")

    with col4:
        dur = metrics['avg_duration']
        st.metric("Avg Duration", f"{dur:.1f} min" if dur else "N/A")

    st.markdown("---")

    # Individual results
    st.subheader("📊 Individual Responses")

    for i, result in enumerate(results):
        rater = result.get('rater', {})
        summary = result.get('summary', {})

        with st.expander(f"**{rater.get('username', f'Rater {i+1}')}** - PFI: {summary.get('pfi_human', 'N/A'):.2f}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                **Rater Info:**
                - Username: {rater.get('username', 'Unknown')}
                - Favorite Movie: {rater.get('favorite_movie', 'Not selected')}
                - Duration: {result.get('duration_minutes', 'N/A'):.1f} min
                """)

            with col2:
                st.markdown(f"""
                **Summary:**
                - PFI Score: {summary.get('pfi_human', 'N/A'):.2f}
                - Chose A: {summary.get('chose_a_count', 0)}x
                - Chose B: {summary.get('chose_b_count', 0)}x
                - Hard to tell: {summary.get('hard_to_tell_count', 0)}x
                """)

            # Show individual responses
            st.markdown("**Responses:**")
            for resp in result.get('responses', []):
                st.markdown(f"- Scenario {resp.get('scenario_id')}: {resp.get('voice_choice')} ({resp.get('confidence')})")

    st.markdown("---")

    # Export section
    st.subheader("📥 Export Data")

    if st.button("Export All Results as JSON"):
        all_data = {
            'export_date': str(PATHS['repo_root']),
            'total_responses': len(results),
            'aggregate_metrics': metrics,
            'individual_results': results
        }
        st.download_button(
            label="Download JSON",
            data=json.dumps(all_data, indent=2, default=str),
            file_name="vudu_all_results.json",
            mime="application/json"
        )
