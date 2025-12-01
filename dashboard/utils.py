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
    """Calculate aggregate metrics from multiple survey results"""
    if not results:
        return {
            'total_responses': 0,
            'avg_pfi': None,
            'avg_confidence': None,
            'avg_duration': None
        }

    pfi_scores = [r.get('summary', {}).get('pfi_human', 0) for r in results if r.get('summary')]
    confidence_scores = [r.get('summary', {}).get('mean_confidence', 0) for r in results if r.get('summary')]
    durations = [r.get('duration_minutes', 0) for r in results if r.get('duration_minutes')]

    return {
        'total_responses': len(results),
        'avg_pfi': sum(pfi_scores) / len(pfi_scores) if pfi_scores else None,
        'avg_confidence': sum(confidence_scores) / len(confidence_scores) if confidence_scores else None,
        'avg_duration': sum(durations) / len(durations) if durations else None
    }
