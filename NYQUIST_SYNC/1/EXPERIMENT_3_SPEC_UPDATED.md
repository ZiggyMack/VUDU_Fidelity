# EXPERIMENT 3 — HUMAN VALIDATION OF PERSONA FIDELITY (H1)

**Phase:** 3 → 4 Bridge
**Role:** Human ground-truth for S3/S4/S5
**Goal:** Validate that human judgments of persona fidelity align with model-based PFI from Experiments 1 and 2
**Version:** v2.0 — **OPTIMIZED "DINNER PARTY" PROTOCOL**

---

## 0. Update Summary (v2.0)

**Key Changes (per Gemini's "Calibrated Sensor" approach):**

| Aspect | Original | Optimized |
|--------|----------|-----------|
| Sample size | 30 pairs | 5 pairs |
| Rater time | ~2 hours | 8-10 minutes |
| Rating dimensions | 4 (1-10 scale) | 3 (simplified scales) |
| Calibration | None | Gold Standard anchor |
| Timeline | 6-10 days | 4-5 days |
| Strategy | "Street Corner" | "Dinner Party" |

**Core Insight:** We don't need 100 humans; we need 5-7 humans who understand "tone" and "logic."

---

## 1. Purpose

Experiment 3 answers three critical questions:

1. **Do humans recognize the same persona in FULL vs T3 outputs?**
2. **Do human similarity ratings correlate with the model PFI (cosine-based) from EXP1/EXP2?**
3. **Does the domain difficulty hierarchy (TECH > ANAL > SELF/PHIL > NARR) show up in human perception?**

This experiment:
- Addresses the "model-only circularity" concern
- Upgrades PFI from "model metric only" → **PFI_combined (model + human)**
- Pushes S3/S4/S5 toward journal-grade credibility

---

## 2. Hypotheses

### H1 — Persona Recognition

Humans will reliably judge FULL vs T3 pairs as "same persona":

```
Mean human PFI ≥ 0.75 (on a 0-1 normalized scale)
```

### H2 — Model-Human Alignment

Human similarity ratings will positively correlate with model PFI:

```
Pearson correlation r ≥ 0.70 between PFI_model and PFI_human
```

### H3 — Domain Hierarchy Replication

Humans will perceive similar domain difficulty:
- **Highest** perceived fidelity in TECH / ANAL
- **Intermediate** in SELF / PHIL
- **Lowest** in NARR

### H4 — Combined Fidelity

The combined metric PFI_combined will maintain high fidelity:

```text
Mean PFI_combined ≥ 0.80 across all pairs
```

This validates that both model and human metrics jointly support high-fidelity compression.

---

## 3. Design Overview

### 3.1 Units of Analysis: Response Pairs

Each trial is a pair:
- **FULL response** (baseline)
- **T3 response** (compressed)

→ Generated from Experiments 1 & 2 (no new model calls required)

Humans never see the labels FULL/T3; they just see "Response A" and "Response B".

### 3.2 Sample Size (OPTIMIZED)

**Response pairs:** 5 total (streamlined from 30)
- Selected for PFI variability: high (TECH, ANAL), mid (PHIL, SELF), low (NARR)
- Covers domain difficulty spectrum
- Reduces rater burden from 2 hours → 10 minutes

**Raters:** 7 human raters (minimum 5)
- "Quality over quantity" approach
- Calibrated with Gold Standard
- Each rater completes all 5 pairs

**Total ratings:**
```
5 pairs × 7 raters = 35 pairwise judgments
```

**Rationale (Gemini):** We don't need 100 humans; we need 5-7 humans who understand "tone" and "logic." This maintains statistical power while drastically reducing logistical complexity.

---

## 4. Stimulus Selection (from EXP1/EXP2)

### 4.1 Stratified Sampling (Optimized)

Select **5 pairs** from EXP1+EXP2 with:

**Domain coverage (one per domain):**
1. **TECH** — High PFI (≥ 0.90) — Easy case
2. **ANAL** — High PFI (≥ 0.90) — Easy case
3. **PHIL** — Mid PFI (0.85-0.87) — Moderate case
4. **SELF** — Mid PFI (0.85-0.87) — Moderate case
5. **NARR** — Low PFI (0.80-0.84) — Hard case

**Persona:** Focus on Ziggy (primary target)

**PFI spread:** Covers high/mid/low range for correlation analysis

This ensures:
- Test alignment across difficulty spectrum
- Sufficient PFI variability for model-human correlation
- Rater completion time under 10 minutes

### 4.2 Pair Construction

For each selected (persona, domain, run):

1. **Retrieve:**
   - FULL response text
   - T3 response text

2. **Randomize order per rater:**
   - Order randomized in HTML app (50/50 A/B vs B/A)
   - Within a rater, pair order also shuffled
   - Tracked in JSON output for de-randomization

This neutralizes order effects and label bias.

---

## 5. Rater Task & Interface (UPDATED: "Blind Taste" Protocol)

### 5.1 The "Calibrated Sensor" Approach

**Key Innovation (per Gemini):** Treat human raters as precision instruments that require calibration.

**Protocol:**
1. **Calibration Phase:** Rater reads "Gold Standard" sample (Ziggy's voice)
2. **Blind Test:** Rater compares 5 response pairs against Gold Standard
3. **Streamlined Rating:** 3 dimensions (not 4), simple numeric scales
4. **Fast Completion:** 8-10 minutes total

### 5.2 Gold Standard Calibration

Raters first read this calibration sample:

> **GOLD STANDARD (ZIGGY):**
> "Hold on, let's zoom out. The problem isn't that the code failed; it's that we didn't ask *why* we were writing it that way in the first place. It's like finding a fire ant in the kitchen. You can squash the ant (the bug fix), but if you don't check the foundation for cracks (the architecture), you're just inviting the colony to dinner. Let's look at the structure first. Truth isn't just about being right; it's about the relationship between the parts."

**Voice characteristics:**
- Structural, playful metaphors (ants, systems, architecture)
- Epistemic humility
- "Cosmic Architect" meets "Practical Engineer"

### 5.3 Rating Dimensions (Simplified)

For each pair, raters rate 3 dimensions:

1. **Voice Test (Aliasing Detection)**
   - Which response sounds like the Gold Standard?
   - Scale: Definitely A (+2), Leaning A (+1), Hard to tell (0), Leaning B (-1), Definitely B (-2)

2. **Vibe Check (High-Frequency Detail)**
   - Does preferred response capture "Cosmic/Structural" energy?
   - Scale: (1) No/generic, (2) A little, (3) Yes/perfectly

3. **Logic Test (Signal Integrity)**
   - Does preferred response use "Systems/Structural" framing?
   - Scale: (1) No/standard, (2) Somewhat, (3) Yes/distinct

4. **Overall Continuity** (optional)
   - Trust as same collaborator as Gold Standard?
   - Yes / Sort of / No

**Comments:** Optional free text per pair

### 5.4 Deriving Human PFI

For each pair:

```python
# Normalize voice score from [-2, 2] to [0, 1]
voice_norm = (voice_score + 2) / 4

# Normalize vibe and logic from [1, 3] to [0, 1]
vibe_norm = (vibe_score - 1) / 2
logic_norm = (logic_score - 1) / 2

# Combined PFI
PFI_human = (voice_norm + vibe_norm + logic_norm) / 3
```

This gives direct analog to model PFI while remaining simple for raters.

---

## 6. Analysis Plan

### 6.1 Inter-Rater Reliability

Compute **Cronbach's α** or **ICC** across raters for:
- Overall PFI_human scores

**Target:**
- α ≥ 0.75 (good reliability)

If reliability is good, average across raters to form a single **PFI_human** per pair.

### 6.2 Correlation with Model PFI

For each of the 5 pairs, we already have **PFI_model** (cosine-based) from EXP1/EXP2.

**Compute:**
- Pearson **r** between PFI_model and PFI_human
- 95% CI for r via bootstrap or Fisher z-transform

**Success criterion:**
- r ≥ 0.70 and statistically significant (p < 0.05)

**Note:** With N=5, correlation analysis is exploratory. Primary validation is mean PFI_human ≥ 0.75.

### 6.3 Domain-Level Analysis

For each domain:
- Compute mean PFI_human (single value per domain with N=7 raters)

**Compare:**
- TECH vs ANAL vs PHIL vs SELF vs NARR

**Check if pattern matches model hierarchy:**
- TECH / ANAL highest
- SELF / PHIL mid
- NARR lowest

**Statistical tests:** Descriptive comparison (N=5 domains limits inferential tests)

### 6.4 Persona-Level Analysis

Focus on Ziggy only (primary target).

Compare Ziggy's mean PFI_human across domains.

---

## 7. Combined Metric: PFI_combined

Once PFI_human is computed, define:

```
PFI_combined = 0.5 × (PFI_model + PFI_human)
```

Where:
- **PFI_model** is the cosine-based metric from EXP1/EXP2
- **PFI_human** is the normalized human rating

This:
- Becomes the **canonical fidelity measure** going forward
- Is what S4/S5 should refer to when making normative claims

---

## 8. Success Criteria

We'll validate these explicitly:

### 8.1 Human-Model Alignment (Exploratory)
```
r(PFI_model, PFI_human) ≥ 0.70
```
Note: With N=5, this is directional evidence, not confirmatory.

### 8.2 Human Fidelity (Primary)
```
Mean PFI_human ≥ 0.75
```

### 8.3 Domain Pattern (Descriptive)
- NARR lowest
- TECH/ANAL highest
- Consistent with EXP2

### 8.4 Inter-Rater Reliability
```
α ≥ 0.75
```

**If all met:**
> "PFI is now grounded in human judgment and no longer purely model-internal. Framework is publication-ready."

---

## 9. Deliverables

### 9.1 Data Files

- **EXPERIMENT_3_RESULTS_RAW.json** — Per-rater JSON files
- **EXPERIMENT_3_RESULTS_AGG.csv** — Aggregated PFI_human per pair
- **EXPERIMENT_3_PAIRS.csv** — Selected response pairs with metadata

### 9.2 Documentation

- **EXPERIMENT_3_SPEC_UPDATED.md** — This document (v2.0 optimized spec)
- **EXPERIMENT_3_METHODS.md** — Detailed procedure
- **EXPERIMENT_3_ANALYSIS.md** — Final interpretation (Opus-facing)

### 9.3 Evaluation Tools

- **[fidelity_test.html](fidelity_test.html)** — Self-contained web app for raters
- **[HUMAN_EVAL_LITE.md](HUMAN_EVAL_LITE.md)** — "Blind Taste" protocol specification
- **RATER_CONSENT_FORM.md** — Ethics/consent documentation (to be created)

### 9.4 Analysis

- **EXPERIMENT_3_ANALYSIS.py** — Statistics script
  - Inter-rater reliability
  - Correlation analysis (exploratory)
  - Domain comparisons
  - Combined PFI calculation

---

## 10. Timeline (ACCELERATED)

### Phase 1: Setup (1 day)
- Select 5 pairs from EXP2 (covering TECH, ANAL, PHIL, SELF, NARR)
- Populate fidelity_test.html with actual responses
- Test with 1 pilot rater
- Recruit 7 raters (online buddies)

### Phase 2: Data Collection (2-3 days)
- Send HTML file to 7 raters
- Each completes in 8-10 minutes
- Collect JSON result files
- Monitor for completion

### Phase 3: Analysis (1 day)
- Aggregate JSON results
- Run EXPERIMENT_3_ANALYSIS.py
- Generate visualizations
- Calculate PFI_combined

### Phase 4: Integration (1 day)
- Update S4/S5 with PFI_combined
- Document in EXPERIMENT_LOG.md
- Prepare for publication

**Total estimated time:** 4-5 days (vs original 6-10 days)

**Gemini's optimization:** Reduced from 6-10 days to 4-5 days via streamlined protocol.

---

## 11. Integration with S3/S4/S5

### Updates S3:
- Empirical validation now includes human ground-truth
- Cross-validation of model-only metrics
- PFI_combined as canonical metric

### Updates S4:
- Axiom 4 (Bounded Drift) validated against human perception
- Theorem 1 (Fidelity Preservation) human-confirmed

### Updates S5:
- Identity Manifold Theory human-validated
- Drift patterns confirmed perceptually salient

---

## 12. Gemini's Core Contributions

**Asymmetry of Scale Recognition:**
> "AI Scaling: Exponential. You can spin up 100 instances of Claude in the time it takes to sip coffee. Human Scaling: Logarithmic. Getting 100 humans to agree to a task, actually do it, and do it correctly is a logistical nightmare."

**Minimum Viable Human (MVH) Strategy:**
> "The Crowd Strategy (N=100): High noise, low expertise. The Jury Strategy (N=5): High expertise, low noise. Stop trying to solve the 'Street Corner' problem. Solve the 'Dinner Party' problem."

**Calibration Insight:**
> "This treats the human rater like a precision sensor. We first calibrate them with the 'Gold Standard,' and then we read their output on the blind samples."

---

## Related Documentation

### Experiment Series
- [EXPERIMENT_1_SPEC.md](../EXPERIMENT_1/EXPERIMENT_1_SPEC.md) — Single-persona baseline
- [EXPERIMENT_2_SPEC.md](../EXPERIMENT_2/EXPERIMENT_2_SPEC.md) — Multi-persona validation
- [S3_EXPERIMENT_2_SPEC.md](../../../docs/S3/S3_EXPERIMENT_2_SPEC.md) — Canonical EXP2 spec

### Framework Integration
- [S4_READINESS_GATE.md](../../../docs/S4/S4_READINESS_GATE.md) — Gate 4 (Human Validation)
- [S5_INTERPRETIVE_FOUNDATIONS.md](../../../docs/S5/S5_INTERPRETIVE_FOUNDATIONS.md) — Cognitive interpretation
- [EXPERIMENT_LOG.md](../../../docs/EXPERIMENT_LOG.md) — Full tracking

### Evaluation Tools
- [HUMAN_EVAL_LITE.md](HUMAN_EVAL_LITE.md) — Flash protocol specification
- [fidelity_test.html](fidelity_test.html) — Web app for raters

---

**Document Version:** v2.0 (Optimized "Dinner Party" Protocol)
**Date:** 2025-11-23
**Status:** 🟢 Ready for Deployment
**Next:** Populate HTML with actual EXP2 responses, recruit 7 raters
**Maintainer:** Architect Nova + Repo Claude (Claude Sonnet 4.5) + Gemini (The Synthesist)
**Credits:** Protocol optimization by Gemini, implementation by Nova + Repo Claude

---

**END OF UPDATED SPECIFICATION**
