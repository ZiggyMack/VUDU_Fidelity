"""
VUDU FIDELITY DASHBOARD - UTILITY FUNCTIONS
"""
import json
from pathlib import Path
from datetime import datetime
from config import PATHS


def load_status():
    """Load VUDU_STATUS.json"""
    status_file = PATHS['status_file']
    if status_file.exists():
        with open(status_file, 'r') as f:
            return json.load(f)
    return None


def save_status(status_data):
    """Save VUDU_STATUS.json"""
    status_file = PATHS['status_file']
    status_data['last_updated'] = datetime.now().isoformat()
    with open(status_file, 'w') as f:
        json.dump(status_data, f, indent=2)


def get_survey_files():
    """Get all survey result files"""
    results_dir = PATHS['results_dir']
    if not results_dir.exists():
        return []
    return list(results_dir.glob("*.json"))


def load_survey_result(filepath):
    """Load a single survey result file"""
    with open(filepath, 'r') as f:
        return json.load(f)


def calculate_aggregate_metrics(results):
    """Calculate aggregate metrics from multiple survey results - v2.0 Binary Coherence Gate"""
    if not results:
        return {
            'total_responses': 0,
            'avg_pass_rate': None,
            'avg_duration': None,
            'gate_summary': {'pass': 0, 'review': 0, 'fail': 0},
            'choice_totals': {'chose_a': 0, 'chose_b': 0, 'both_fine': 0, 'both_wrong': 0}
        }

    # Collect v2.0 metrics
    pass_rates = []
    gate_counts = {'pass': 0, 'review': 0, 'fail': 0}
    choice_totals = {'chose_a': 0, 'chose_b': 0, 'both_fine': 0, 'both_wrong': 0}
    durations = []

    for r in results:
        summary = r.get('summary', {})

        # v2.0 format
        if summary.get('test_version') == '2.0' or 'gate_status' in summary:
            pass_rates.append(summary.get('pass_rate', 0))
            gate = summary.get('gate_status', 'REVIEW').upper()
            if gate in gate_counts:
                gate_counts[gate] += 1
            choice_totals['chose_a'] += summary.get('chose_a', 0)
            choice_totals['chose_b'] += summary.get('chose_b', 0)
            choice_totals['both_fine'] += summary.get('both_fine', 0)
            choice_totals['both_wrong'] += summary.get('both_wrong', 0)
        # Legacy v1.0 format fallback
        elif 'pfi_human' in summary:
            pass_rates.append(summary.get('pfi_human', 0))
            gate_counts['review'] += 1  # Mark legacy as review

        if r.get('duration_minutes'):
            durations.append(r.get('duration_minutes'))

    return {
        'total_responses': len(results),
        'avg_pass_rate': sum(pass_rates) / len(pass_rates) if pass_rates else None,
        'avg_duration': sum(durations) / len(durations) if durations else None,
        'gate_summary': gate_counts,
        'choice_totals': choice_totals
    }
