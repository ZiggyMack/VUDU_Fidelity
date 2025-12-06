"""
Results Page - Survey Results and Analysis (v2.0 Binary Coherence Gate)
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
    st.markdown("*EXP3 v2.0 - Binary Coherence Gate Results*")
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

        # Show sample result structure for v2.0
        st.subheader("📋 Expected Result Format (v2.0)")
        sample = {
            "test_version": "2.0",
            "protocol": "Binary Coherence Gate",
            "rater": {"username": "example_rater", "favorite_movie": "The Matrix"},
            "completed_at": "2025-12-01T12:00:00",
            "duration_minutes": 10.5,
            "responses": [{"scenario_id": 1, "choice": "Response A", "comments": ""}],
            "summary": {
                "test_version": "2.0",
                "protocol": "Binary Coherence Gate",
                "total_scenarios": 5,
                "chose_a": 3,
                "chose_b": 1,
                "both_fine": 1,
                "both_wrong": 0,
                "pass_rate": 0.80,
                "gate_status": "PASS"
            }
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

    # Display metrics - v2.0 Binary Coherence Gate format
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Responses", metrics['total_responses'])

    with col2:
        pass_rate = metrics['avg_pass_rate']
        st.metric("Avg Pass Rate", f"{pass_rate:.0%}" if pass_rate else "N/A")

    with col3:
        gate = metrics['gate_summary']
        st.metric("Gate Results", f"✓{gate['pass']} ⚠{gate['review']} ✗{gate['fail']}")

    with col4:
        dur = metrics['avg_duration']
        st.metric("Avg Duration", f"{dur:.1f} min" if dur else "N/A")

    # Choice breakdown
    st.markdown("---")
    st.subheader("📊 Choice Distribution")

    choice_totals = metrics['choice_totals']
    total_choices = sum(choice_totals.values())

    if total_choices > 0:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            pct = choice_totals['chose_a'] / total_choices * 100
            st.metric("Response A", f"{choice_totals['chose_a']} ({pct:.0f}%)")
        with col2:
            pct = choice_totals['chose_b'] / total_choices * 100
            st.metric("Response B", f"{choice_totals['chose_b']} ({pct:.0f}%)")
        with col3:
            pct = choice_totals['both_fine'] / total_choices * 100
            st.metric("Can't Tell", f"{choice_totals['both_fine']} ({pct:.0f}%)")
        with col4:
            pct = choice_totals['both_wrong'] / total_choices * 100
            st.metric("Both Wrong", f"{choice_totals['both_wrong']} ({pct:.0f}%)")

    st.markdown("---")

    # Individual results
    st.subheader("📋 Individual Responses")

    for i, result in enumerate(results):
        rater = result.get('rater', {})
        summary = result.get('summary', {})

        # Get gate status for display
        gate_status = summary.get('gate_status', 'N/A')
        gate_icon = "✓" if gate_status == "PASS" else ("⚠" if gate_status == "REVIEW" else "✗")

        with st.expander(f"**{rater.get('username', f'Rater {i+1}')}** - {gate_icon} {gate_status}"):
            col1, col2 = st.columns(2)

            with col1:
                duration = result.get('duration_minutes', 0)
                st.markdown(f"""
                **Rater Info:**
                - Username: {rater.get('username', 'Unknown')}
                - Favorite Movie: {rater.get('favorite_movie', 'Not selected')}
                - Duration: {duration:.1f} min
                """)

            with col2:
                st.markdown(f"""
                **Summary (v2.0):**
                - Gate Status: **{gate_status}**
                - Pass Rate: {summary.get('pass_rate', 0):.0%}
                - Response A: {summary.get('chose_a', 0)}x
                - Response B: {summary.get('chose_b', 0)}x
                - Can't Tell: {summary.get('both_fine', 0)}x
                - Both Wrong: {summary.get('both_wrong', 0)}x
                """)

            # Show individual responses
            st.markdown("**Responses:**")
            for resp in result.get('responses', []):
                choice = resp.get('choice', resp.get('voice_choice', 'N/A'))
                comments = resp.get('comments', '')
                comment_text = f" - *{comments}*" if comments else ""
                st.markdown(f"- Scenario {resp.get('scenario_id')}: {choice}{comment_text}")

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
