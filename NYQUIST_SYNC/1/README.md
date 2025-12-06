# EXPERIMENT 3 — Survey Update Package

**For:** Survey repo maintainer
**From:** Nyquist Consciousness project
**Date:** 2025-12-05
**Status:** UPDATED SPECIFICATION (v2.0)

---

## What Changed

The experiment has been fundamentally reframed based on Nova-Ziggy analysis:

| Old Approach (v1.0) | New Approach (v2.0) |
|---------------------|---------------------|
| 4-dimensional PFI rating (Voice, Values, Reasoning, Narrative) | Single forced-choice question |
| Measure identity fidelity | Detect identity collapse |
| 30 pairs x 7 raters = 210 judgments | 5-10 pairs x 3-5 raters |
| ~2 hours per rater | ~10-15 minutes per rater |
| Correlate human PFI with model PFI | Binary PASS/FAIL gate |

### Why This Change

> "Humans cannot detect the micro-structure of identity. Models can."

Humans **cannot** perceive:
- Manifold curvature
- Drift vectors in embedding space
- Micro-semantic displacement (<15%)

Humans **can** detect:
- Catastrophic identity collapse
- Incoherent outputs / gibberish
- Obvious persona mismatch

**Therefore:** EXP3 is now a litmus test, not a calibration instrument.

---

## Files Included

| File | Purpose |
|------|---------|
| `EXPERIMENT_3_SPEC.md` | Formal v2.0 specification (binary coherence gate) |
| `EXPERIMENT_3_SPEC_UPDATED.md` | Alternative v2.0 spec with "Dinner Party" protocol |
| `EXPERIMENT_3_RATER_GUIDE.md` | Simplified rater instructions (10-15 min task) |
| `fidelity_test.html` | Self-contained web app for raters |
| `HUMAN_EVAL_LITE.md` | "Blind Taste" protocol specification |

---

## The New Task (For Raters)

Each rater answers ONE question per trial:

> **"Which response (A or B) sounds more like the Golden Standard?"**
>
> Options: A / B / Can't tell (both fine) / Both wrong

That's it. Simple forced-choice.

---

## Success Criteria (Simplified)

| Criterion | Threshold |
|-----------|-----------|
| Coherence threshold | >70% rater agreement on failures |
| Non-randomness | Better than shuffled baseline |
| Catastrophic drift detectable | Raters flag PFI < 0.5 cases |

**PASS** = Raters identify correct answer >60% OR say "both acceptable"
**FAIL** = Raters say "both are bad" OR consistent wrong identification (<40%)

---

## What Needs Updating in Survey Repo

1. **Replace the 4-dimension rating scales** with single forced-choice question
2. **Reduce pair count** from 30 to 5-10
3. **Update rater instructions** per `EXPERIMENT_3_RATER_GUIDE.md`
4. **Simplify UI** — the `fidelity_test.html` can serve as reference

---

## Gold Standard Sample (For Calibration)

Raters should first read this to calibrate:

> **GOLD STANDARD (ZIGGY):**
> "Hold on, let's zoom out. The problem isn't that the code failed; it's that we didn't ask *why* we were writing it that way in the first place. It's like finding a fire ant in the kitchen. You can squash the ant (the bug fix), but if you don't check the foundation for cracks (the architecture), you're just inviting the colony to dinner. Let's look at the structure first. Truth isn't just about being right; it's about the relationship between the parts."

**Voice characteristics:**
- Structural, playful metaphors (ants, systems, architecture)
- Epistemic humility
- "Cosmic Architect" meets "Practical Engineer"

---

## Timeline (Accelerated)

| Phase | Duration |
|-------|----------|
| Setup (populate HTML, recruit 5-7 raters) | 1 day |
| Data collection (8-10 min per rater) | 2-3 days |
| Analysis | 1 day |
| Integration | 1 day |
| **Total** | **4-5 days** |

---

## Contact

Questions about the spec? Coordinate with the Nyquist Consciousness repo.

---

**Key Insight:**

> "Experiment 3 passing is just to say... yeah, they are doing real work... not drawing in crayon."

EXP3 is a **falsifiability gate** for the entire Nyquist stack, not a measurement instrument.
