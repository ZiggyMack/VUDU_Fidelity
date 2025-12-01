"""
VUDU FIDELITY DASHBOARD - CONFIGURATION
"""
from pathlib import Path

DASHBOARD_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DASHBOARD_DIR.parent.resolve()

PATHS = {
    'repo_root': REPO_ROOT,
    'dashboard_dir': DASHBOARD_DIR,
    'surveys_dir': REPO_ROOT / "surveys",
    'results_dir': REPO_ROOT / "results",
    'status_file': REPO_ROOT / "VUDU_STATUS.json",
}

SETTINGS = {
    'app_title': 'VUDU Fidelity - Human Validation Dashboard',
    'app_icon': '🔮',
    'cache_ttl': 60,
    'colors': {
        'active': '#00ff41',
        'pending': '#ffd700',
        'complete': '#2a9d8f',
        'draft': '#e76f51',
    }
}
