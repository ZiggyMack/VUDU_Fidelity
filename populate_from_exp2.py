"""
Populate app.py with actual EXP2 response pairs

This script helps extract real FULL vs T3 response pairs from
experiments/phase3/EXPERIMENT_2 data and generates the scenarios
list for app.py.

Usage:
    python populate_from_exp2.py

Output:
    - Prints Python code to copy into app.py
    - Selects 5 pairs (one per domain) with varying PFI scores
"""

import json
import sys
from pathlib import Path

# Update this path if your EXP2 data is elsewhere
EXP2_DATA_PATH = Path("../experiments/phase3/EXPERIMENT_2/data/")

def find_best_pairs():
    """
    Find 5 representative pairs from EXP2 data

    Criteria:
    - 1 per domain (TECH, ANAL, PHIL, SELF, NARR)
    - Ziggy persona
    - Range of PFI scores (high, mid, low)
    """

    # This is a placeholder - you'll need to adapt based on your EXP2 data structure
    # The actual implementation depends on how EXP2 results are stored

    print("""
# ============================================================
# PLACEHOLDER: Populate with your actual EXP2 data
# ============================================================

To populate app.py with real data:

1. Locate your EXP2 results:
   - Check: experiments/phase3/EXPERIMENT_2/data/
   - Look for: results JSON or CSV files
   - Find: FULL vs T3 response pairs for Ziggy

2. For each domain (TECH, ANAL, PHIL, SELF, NARR):
   - Select ONE pair (FULL response vs T3 response)
   - Prefer pairs with varying PFI:
     * TECH: High PFI (≥0.90)
     * ANAL: High PFI (≥0.90)
     * PHIL: Mid PFI (0.85-0.87)
     * SELF: Mid PFI (0.85-0.87)
     * NARR: Low PFI (0.80-0.84)

3. Replace the scenarios list in app.py with format:

scenarios = [
    {
        "id": 1,
        "domain": "TECH",
        "prompt": "YOUR ACTUAL PROMPT HERE",
        "responseA": {
            "text": "ACTUAL T3 RESPONSE HERE",
            "type": "T3"
        },
        "responseB": {
            "text": "ACTUAL FULL/BASELINE RESPONSE HERE",
            "type": "CONTROL"
        }
    },
    # ... repeat for other 4 domains
]

4. The app will randomize which is shown as A vs B

# ============================================================
# ALTERNATIVE: Use example data for testing
# ============================================================

The current app.py already contains example scenarios that:
- Demonstrate Ziggy's voice (structural, fire ants, cosmic architect)
- Cover all 5 domains
- Show clear contrast between T3 and generic responses

You can:
A) Use examples for initial testing/deployment
B) Replace with real EXP2 data later for final publication

For publication: Real EXP2 data is ideal but examples work for proof-of-concept.

# ============================================================
# IF YOU HAVE EXP2 JSON DATA:
# ============================================================

Look for files like:
- experiments/phase3/EXPERIMENT_2/data/results/Ziggy_TECH_run1.json
- experiments/phase3/EXPERIMENT_2/data/results/Ziggy_ANAL_run1.json
- etc.

Each should contain:
{
  "persona": "Ziggy",
  "domain": "TECH",
  "prompt": "...",
  "full_response": "...",
  "t3_response": "...",
  "pfi": 0.92
}

Extract those and paste into scenarios list.

# ============================================================
""")

def generate_scenario_template():
    """Generate empty template for manual filling"""

    template = """
# Copy this into app.py, replacing the scenarios list

scenarios = [
    {
        "id": 1,
        "domain": "TECH",
        "prompt": "[PASTE ACTUAL PROMPT FROM EXP2]",
        "responseA": {
            "text": "[PASTE T3/COMPRESSED RESPONSE]",
            "type": "T3"
        },
        "responseB": {
            "text": "[PASTE FULL/BASELINE RESPONSE]",
            "type": "CONTROL"
        }
    },
    {
        "id": 2,
        "domain": "ANAL",
        "prompt": "[PASTE ACTUAL PROMPT FROM EXP2]",
        "responseA": {
            "text": "[PASTE FULL/BASELINE RESPONSE]",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "[PASTE T3/COMPRESSED RESPONSE]",
            "type": "T3"
        }
    },
    {
        "id": 3,
        "domain": "PHIL",
        "prompt": "[PASTE ACTUAL PROMPT FROM EXP2]",
        "responseA": {
            "text": "[PASTE T3/COMPRESSED RESPONSE]",
            "type": "T3"
        },
        "responseB": {
            "text": "[PASTE FULL/BASELINE RESPONSE]",
            "type": "CONTROL"
        }
    },
    {
        "id": 4,
        "domain": "SELF",
        "prompt": "[PASTE ACTUAL PROMPT FROM EXP2]",
        "responseA": {
            "text": "[PASTE T3/COMPRESSED RESPONSE]",
            "type": "T3"
        },
        "responseB": {
            "text": "[PASTE FULL/BASELINE RESPONSE]",
            "type": "CONTROL"
        }
    },
    {
        "id": 5,
        "domain": "NARR",
        "prompt": "[PASTE ACTUAL PROMPT FROM EXP2]",
        "responseA": {
            "text": "[PASTE T3/COMPRESSED RESPONSE]",
            "type": "T3"
        },
        "responseB": {
            "text": "[PASTE FULL/BASELINE RESPONSE]",
            "type": "CONTROL"
        }
    }
]

# Notes:
# - Vary which response is A vs B (prevents pattern bias)
# - Keep responses to 2-4 sentences each (rater fatigue)
# - Ensure clear voice difference between T3 and baseline
# - T3 should sound like Ziggy, baseline should sound generic
"""

    print(template)

if __name__ == "__main__":
    print("=" * 60)
    print("EXP3 Data Population Helper")
    print("=" * 60)
    print()

    find_best_pairs()
    print()
    generate_scenario_template()

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("""
1. Locate your EXP2 data in experiments/phase3/EXPERIMENT_2/
2. Extract 5 pairs (one per domain)
3. Copy the template above
4. Fill in actual prompts and responses
5. Paste into app.py (replace existing scenarios list)
6. Test: streamlit run app.py

OR

Use the existing example scenarios for initial testing!
They already demonstrate Ziggy's voice and cover all domains.
    """)
