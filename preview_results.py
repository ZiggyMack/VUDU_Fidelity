"""
Preview EXP3 Results

Quick analysis of collected rater JSON files.
Run this as results come in to monitor progress.

Usage:
    python preview_results.py
"""

import json
from pathlib import Path
from statistics import mean, stdev

def load_results():
    """Load all JSON results from results/ folder"""
    results_dir = Path("results")
    json_files = list(results_dir.glob("*.json"))

    if not json_files:
        print("No results found in results/ folder")
        return []

    results = []
    for file in json_files:
        with open(file, 'r') as f:
            results.append(json.load(f))

    return results

def analyze_results(results):
    """Analyze collected results"""
    if not results:
        return

    print("=" * 60)
    print(f"EXP3 RESULTS PREVIEW ({len(results)} raters)")
    print("=" * 60)
    print()

    # Overall stats
    print("Overall Statistics:")
    print("-" * 60)

    all_pfis = [r['summary']['pfi_human'] for r in results]
    print(f"  Raters completed: {len(results)}/7")
    print(f"  Mean PFI_human: {mean(all_pfis):.3f}")
    if len(all_pfis) > 1:
        print(f"  Std Dev: {stdev(all_pfis):.3f}")
    print(f"  Range: {min(all_pfis):.3f} - {max(all_pfis):.3f}")
    print()

    # Success criteria check
    print("Success Criteria:")
    print("-" * 60)
    mean_pfi = mean(all_pfis)
    target_pfi = 0.75

    status = "✅ PASS" if mean_pfi >= target_pfi else "❌ FAIL"
    print(f"  Mean PFI ≥ 0.75: {status} (actual: {mean_pfi:.3f})")

    if len(results) >= 5:
        print(f"  ✅ Minimum raters met (5+)")
    else:
        print(f"  ⚠️  Need more raters ({len(results)}/5 minimum)")
    print()

    # Per-domain analysis
    print("Domain-Level Analysis:")
    print("-" * 60)

    # Aggregate by domain
    domain_scores = {
        'TECH': [],
        'ANAL': [],
        'PHIL': [],
        'SELF': [],
        'NARR': []
    }

    for result in results:
        for response in result['responses']:
            domain = response['domain']
            # Calculate PFI for this response
            voice_norm = (response['voice_score'] + 2) / 4
            vibe_norm = (response['vibe_score'] - 1) / 2
            logic_norm = (response['logic_score'] - 1) / 2
            pfi = (voice_norm + vibe_norm + logic_norm) / 3

            domain_scores[domain].append(pfi)

    for domain in ['TECH', 'ANAL', 'PHIL', 'SELF', 'NARR']:
        scores = domain_scores[domain]
        if scores:
            print(f"  {domain}: {mean(scores):.3f} (n={len(scores)})")

    print()

    # Expected pattern check
    print("Domain Hierarchy (Expected: TECH/ANAL > SELF/PHIL > NARR):")
    print("-" * 60)
    domain_means = {d: mean(scores) for d, scores in domain_scores.items() if scores}

    if domain_means:
        sorted_domains = sorted(domain_means.items(), key=lambda x: x[1], reverse=True)
        for i, (domain, score) in enumerate(sorted_domains, 1):
            print(f"  {i}. {domain}: {score:.3f}")
    print()

    # Duration stats
    print("Completion Times:")
    print("-" * 60)
    durations = [r['duration_minutes'] for r in results]
    print(f"  Mean: {mean(durations):.1f} minutes")
    print(f"  Range: {min(durations):.1f} - {max(durations):.1f} minutes")
    target_duration = 8
    if mean(durations) <= 12:
        print(f"  ✅ Within target (8-10 min)")
    else:
        print(f"  ⚠️  Longer than expected (>12 min)")
    print()

    # Next steps
    print("Next Steps:")
    print("-" * 60)
    if len(results) < 5:
        print(f"  🔲 Recruit {5 - len(results)} more rater(s) (minimum)")
    elif len(results) < 7:
        print(f"  🔲 Recruit {7 - len(results)} more rater(s) (target)")
    else:
        print(f"  ✅ All raters complete!")

    if len(results) >= 5:
        print(f"  🔲 Copy results to main EXP3 folder:")
        print(f"     cp results/*.json ../experiments/phase3/EXPERIMENT_3/data/results/")
        print(f"  🔲 Run full analysis:")
        print(f"     cd ../experiments/phase3/EXPERIMENT_3/")
        print(f"     python EXPERIMENT_3_ANALYSIS.py")

    print()
    print("=" * 60)

def main():
    results = load_results()

    if not results:
        print("\n📂 No results found yet.")
        print("\nResults will appear here as raters complete the test.")
        print("Each rater downloads a JSON file and sends it to you.")
        print("Place those files in the results/ folder.\n")
        return

    analyze_results(results)

if __name__ == "__main__":
    main()
