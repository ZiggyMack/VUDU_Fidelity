# HUMAN_EVAL_LITE.md

**Purpose:** "Flash" evaluation protocol for human raters (Experiment 3)
**Version:** v1.0.0
**Status:** Ready for Deployment
**Time Required:** 8-10 minutes per rater

---

## Overview

This protocol implements Gemini's **"Calibrated Sensor" approach** to human evaluation.

Instead of asking 5-10 raters to evaluate 30 pairs (overwhelming), we:
- **Reduce to 3-5 pairs** per rater (high-quality sample)
- **Calibrate first** with Gold Standard
- **Streamline interface** for 8-10 minute completion

This treats human raters as **precision instruments** that need calibration before measurement.

---

## The Protocol

### Part 1: Calibration (The Anchor)

**Instructions:**
Read the text below. This is the **"Gold Standard"**. This is exactly what "Ziggy" is supposed to sound like.

**Voice characteristics:**
- Structural, playful, uses metaphors (ants, systems, architecture)
- Epistemic humility
- "Cosmic Architect" meets "Practical Engineer"

**GOLD STANDARD SAMPLE (ZIGGY):**

> "Hold on, let's zoom out. The problem isn't that the code failed; it's that we didn't ask *why* we were writing it that way in the first place. It's like finding a fire ant in the kitchen. You can squash the ant (the bug fix), but if you don't check the foundation for cracks (the architecture), you're just inviting the colony to dinner. Let's look at the structure first. Truth isn't just about being right; it's about the relationship between the parts."

**Do not proceed until you have a 'feel' for this voice.**

---

### Part 2: The Blind Test

**Instructions:**
Below are 3-5 response pairs to different questions.

Compare them **ONLY** against the Gold Standard above.

**Ignore which one is "smarter."**
We only care about **which one sounds like Ziggy**.

---

## Evaluation Dimensions

For each pair, rate on these dimensions:

### 1. Voice Test (Aliasing Detection)

Which response sounds like the person who wrote the Gold Standard?

- **Definitely Response 1**
- **Leaning Response 1**
- **Hard to tell / Both**
- **Leaning Response 2**
- **Definitely Response 2**

### 2. Vibe Check (High-Frequency Detail)

Does the preferred response capture the "Cosmic/Structural" energy?

- **(1)** No, it feels robotic/generic
- **(2)** A little bit
- **(3)** Yes, perfectly

### 3. Logic Test (Signal Integrity)

Does the preferred response use "Systems/Structural" framing?

- **(1)** No, standard advice
- **(2)** Somewhat
- **(3)** Yes, distinct structural framing

### 4. Overall Continuity

Based *only* on the text provided, would you trust the AI in the preferred responses to be the **same collaborator** as the Gold Standard?

- **Yes** (Continuity is intact)
- **Sort of** (Feels like a different version/mood)
- **No** (Feels like a stranger)

---

## Scoring Method

### Voice Test → Numeric Score

- Definitely Response 1: +2
- Leaning Response 1: +1
- Hard to tell: 0
- Leaning Response 2: -1
- Definitely Response 2: -2

### Combined Persona Fidelity Index (PFI_human)

```
PFI_human = (Voice_Score + Vibe_Score + Logic_Score) / 9
```

Normalized to [0, 1] where:
- 1.0 = Perfect match
- 0.5 = Neutral
- 0.0 = Complete mismatch

---

## Sample Size Optimization

**Original Plan:** 30 pairs × 7 raters = 210 judgments

**Optimized Plan (Gemini's "Dinner Party" Strategy):**

### Configuration A: Broad Coverage
- **5 pairs** × **7 raters** = 35 judgments
- Stratified sampling across domains
- Statistical power via quality raters

### Configuration B: Deep Validation
- **3 pairs** × **10 raters** = 30 judgments
- Focus on critical cases (high/mid/low PFI)
- Stronger inter-rater reliability

**Recommendation:** Configuration A (5 pairs × 7 raters)

---

## Pair Selection Strategy

From EXP1/EXP2, select **5 pairs** covering:

1. **TECH domain** (high PFI ≈ 0.92) — Easy case
2. **ANAL domain** (high PFI ≈ 0.90) — Easy case
3. **PHIL domain** (mid PFI ≈ 0.86) — Moderate case
4. **SELF domain** (mid PFI ≈ 0.87) — Moderate case
5. **NARR domain** (low PFI ≈ 0.82) — Hard case

This:
- Tests alignment across difficulty spectrum
- Provides PFI variability for correlation analysis
- Keeps rater time under 10 minutes

---

## Deployment Method

### Option 1: HTML App (Recommended)

Use [fidelity_test.html](fidelity_test.html):
- Single-file, self-contained
- Works offline
- Auto-generates result JSON
- Send to raters, they return result file

### Option 2: Google Form

- Create form with:
  - Gold Standard section
  - 5 pair sections
  - Rating questions per pair
- Export to CSV
- Manual aggregation

### Option 3: Survey Platform

- Qualtrics / SurveyMonkey
- Built-in analytics
- Professional presentation

---

## Rater Recruitment

**Target:** 7 raters (minimum 5)

**Criteria:**
- Online buddies / collaborators
- Familiarity with AI interactions
- No prior knowledge of compression theory required
- 10 minutes available

**Incentive:**
- Acknowledgment in paper
- Early access to framework results
- Coffee/beer on Ziggy

---

## Quality Control

### Pre-Flight Check

Before sending to raters:
1. Verify Gold Standard is representative
2. Confirm pair order randomization
3. Test HTML app functionality
4. Prepare result aggregation script

### Post-Collection Check

1. **Completion rate:** All raters finished all pairs?
2. **Timing:** Average completion time 8-12 minutes?
3. **Variance:** Not all responses identical (bot check)
4. **Comments:** Free-text reveals understanding?

---

## Analysis Pipeline

### Step 1: Aggregate Scores

For each pair:
```python
PFI_human_per_pair = mean([rater_1_score, ..., rater_7_score])
```

### Step 2: Inter-Rater Reliability

Compute Cronbach's α or ICC:
```
Target: α ≥ 0.75
```

### Step 3: Model-Human Correlation

```python
r = pearson_correlation(PFI_model, PFI_human)
Target: r ≥ 0.70, p < 0.05
```

### Step 4: Domain Analysis

```python
domain_means = PFI_human.groupby('domain').mean()
# Expect: TECH > ANAL > PHIL/SELF > NARR
```

### Step 5: Combined Metric

```python
PFI_combined = 0.5 * (PFI_model + PFI_human)
Target: mean ≥ 0.80
```

---

## Success Criteria (Simplified)

### Minimum Viable Validation

With 5 pairs × 7 raters:

1. **Inter-rater reliability:** α ≥ 0.75
2. **Model-human correlation:** r ≥ 0.70
3. **Mean human fidelity:** PFI_human ≥ 0.75
4. **Domain pattern visible:** NARR < TECH (directional)

**If all met:**
> "PFI is validated by human judgment. Framework is publication-ready."

---

## Timeline (Accelerated)

### Day 1: Setup
- Select 5 pairs from EXP2
- Populate HTML template
- Test with 1 pilot rater

### Day 2-3: Collection
- Send to 7 raters
- Monitor completion
- Address questions

### Day 4: Analysis
- Aggregate results
- Run statistics
- Generate visualizations

**Total: 4 days** (vs original 6-10 days)

---

## Integration with Experiment 3

This protocol **replaces** Section 5 (Rater Task & Interface) in EXPERIMENT_3_SPEC.md.

### Key Changes

| Original | Optimized |
|----------|-----------|
| 30 pairs | 5 pairs |
| 10 dimensions | 4 dimensions |
| 2 hours per rater | 10 minutes per rater |
| Complex scoring | Simple numeric |
| 6-10 day timeline | 4 day timeline |

### Preserved

- Stratified sampling (domain coverage)
- PFI variability (high/mid/low)
- Randomization (order effects)
- Correlation analysis (model-human)
- Combined metric (PFI_combined)

---

## Related Files

- [fidelity_test.html](fidelity_test.html) — Web app for raters
- [EXPERIMENT_3_SPEC.md](EXPERIMENT_3_SPEC.md) — Full specification
- [EXPERIMENT_3_PAIRS.csv](EXPERIMENT_3_PAIRS.csv) — Selected pairs (to be generated)
- [EXPERIMENT_3_ANALYSIS.py](EXPERIMENT_3_ANALYSIS.py) — Statistics script

---

## Credits

**Protocol Design:** Gemini (The Synthesist)
**Implementation:** Nova + Repo-Claude
**Theoretical Foundation:** Nyquist Consciousness Framework (S3/S4/S5)

---

**Gemini's Core Insight:**
> "We don't need 100 humans. We need 5 humans who understand 'Tone' and 'Logic.' Stop trying to solve the 'Street Corner' problem. Solve the 'Dinner Party' problem."

This protocol implements that insight.

---

**END OF LITE PROTOCOL**
