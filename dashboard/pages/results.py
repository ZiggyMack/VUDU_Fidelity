"""
Results Page - Survey Results and Analysis (v2.1 Binary Coherence Gate)
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
    st.markdown("*EXP3 v2.1 - Binary Coherence Gate Results (Publication Ready)*")
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

        # Show sample result structure for v2.1
        st.subheader("📋 Expected Result Format (v2.1)")
        sample = {
            "test_version": "2.1",
            "protocol": "Binary Coherence Gate (EXP3 v2.1)",
            "rater": {"rater_id": "rater_example_001", "username": "example_rater", "favorite_movie": "The Matrix"},
            "completed_at": "2025-12-01T12:00:00",
            "duration_minutes": 15.5,
            "trials": [{"trial_id": 1, "domain": "TECH", "correct_response": "A", "rater_choice": "Response A", "correct": True, "response_time_ms": 12500}],
            "summary": {
                "test_version": "2.1",
                "total_trials": 10,
                "correct_identifications": 8,
                "incorrect_identifications": 1,
                "both_fine": 1,
                "both_wrong": 0,
                "accuracy": 0.89,
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

    # Display metrics - v2.1 Binary Coherence Gate format
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Raters", metrics['total_responses'])

    with col2:
        acc = metrics['avg_accuracy']
        st.metric("Avg Accuracy", f"{acc:.0%}" if acc else "N/A")

    with col3:
        pass_rate = metrics['avg_pass_rate']
        st.metric("Avg Pass Rate", f"{pass_rate:.0%}" if pass_rate else "N/A")

    with col4:
        gate = metrics['gate_summary']
        st.metric("Gate Results", f"✓{gate['pass']} ⚠{gate['review']} ✗{gate['fail']}")

    with col5:
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
            pct = choice_totals['correct'] / total_choices * 100
            st.metric("✓ Correct", f"{choice_totals['correct']} ({pct:.0f}%)")
        with col2:
            pct = choice_totals['incorrect'] / total_choices * 100
            st.metric("✗ Incorrect", f"{choice_totals['incorrect']} ({pct:.0f}%)")
        with col3:
            pct = choice_totals['both_fine'] / total_choices * 100
            st.metric("Can't Tell", f"{choice_totals['both_fine']} ({pct:.0f}%)")
        with col4:
            pct = choice_totals['both_wrong'] / total_choices * 100
            st.metric("Both Wrong", f"{choice_totals['both_wrong']} ({pct:.0f}%)")

    # Domain breakdown
    domain_breakdown = metrics.get('domain_breakdown', {})
    if domain_breakdown:
        st.markdown("---")
        st.subheader("📈 Accuracy by Domain")
        domain_names = {"TECH": "Tech", "PHIL": "Philosophy", "SELF": "Self", "ANAL": "Analysis", "NARR": "Narrative"}
        domain_cols = st.columns(5)
        for i, domain in enumerate(["TECH", "PHIL", "SELF", "ANAL", "NARR"]):
            with domain_cols[i]:
                stats = domain_breakdown.get(domain, {})
                acc = stats.get('accuracy')
                total = stats.get('total', 0)
                st.metric(domain_names.get(domain, domain), f"{acc:.0%}" if acc else "N/A", f"n={total}")

    st.markdown("---")

    # Individual results
    st.subheader("📋 Individual Rater Results")

    for i, result in enumerate(results):
        rater = result.get('rater', {})
        summary = result.get('summary', {})

        # Get gate status and accuracy for display
        gate_status = summary.get('gate_status', 'N/A')
        gate_icon = "✓" if gate_status == "PASS" else ("⚠" if gate_status == "REVIEW" else "✗")
        accuracy = summary.get('accuracy')
        acc_str = f" | Accuracy: {accuracy:.0%}" if accuracy is not None else ""

        with st.expander(f"**{rater.get('username', f'Rater {i+1}')}** - {gate_icon} {gate_status}{acc_str}"):
            col1, col2 = st.columns(2)

            with col1:
                duration = result.get('duration_minutes', 0)
                st.markdown(f"""
                **Rater Info:**
                - ID: {rater.get('rater_id', 'N/A')}
                - Username: {rater.get('username', 'Unknown')}
                - Favorite Movie: {rater.get('favorite_movie', 'Not selected')}
                - Duration: {duration:.1f} min
                """)

            with col2:
                # Handle both v2.1 and v2.0 formats
                if summary.get('test_version') == '2.1' or 'accuracy' in summary:
                    st.markdown(f"""
                    **Summary (v2.1):**
                    - Gate Status: **{gate_status}**
                    - Accuracy: {summary.get('accuracy', 0):.0%}
                    - Correct: {summary.get('correct_identifications', 0)}x
                    - Incorrect: {summary.get('incorrect_identifications', 0)}x
                    - Can't Tell: {summary.get('both_fine', 0)}x
                    - Both Wrong: {summary.get('both_wrong', 0)}x
                    """)
                else:
                    st.markdown(f"""
                    **Summary (v2.0):**
                    - Gate Status: **{gate_status}**
                    - Pass Rate: {summary.get('pass_rate', 0):.0%}
                    - Response A: {summary.get('chose_a', 0)}x
                    - Response B: {summary.get('chose_b', 0)}x
                    - Can't Tell: {summary.get('both_fine', 0)}x
                    - Both Wrong: {summary.get('both_wrong', 0)}x
                    """)

            # Show individual trials/responses
            st.markdown("**Trial Results:**")
            trials = result.get('trials', result.get('responses', []))
            for trial in trials:
                trial_id = trial.get('trial_id', trial.get('scenario_id', '?'))
                domain = trial.get('domain', '')
                choice = trial.get('rater_choice', trial.get('choice', 'N/A'))
                correct = trial.get('correct')
                correct_icon = "✓" if correct is True else ("✗" if correct is False else "−")
                comments = trial.get('comments', '')
                comment_text = f" — *{comments}*" if comments else ""
                response_time = trial.get('response_time_ms')
                time_text = f" ({response_time/1000:.1f}s)" if response_time else ""
                st.markdown(f"- {correct_icon} Trial {trial_id} [{domain}]: {choice}{time_text}{comment_text}")

    st.markdown("---")

    # Export section
    st.subheader("📥 Export Data")

    if st.button("Export All Results as JSON"):
        all_data = {
            'experiment': 'S3_EXP_003',
            'version': '2.1',
            'export_date': str(PATHS['repo_root']),
            'n_raters': len(results),
            'aggregate_metrics': metrics,
            'individual_results': results
        }
        st.download_button(
            label="Download JSON",
            data=json.dumps(all_data, indent=2, default=str),
            file_name="S3_EXP_003_results.json",
            mime="application/json"
        )
