# EXPERIMENT 3 — HUMAN COHERENCE SANITY CHECK

**Version:** 2.0 (Corrected Scientific Specification)
**Phase:** 3 → 4 Bridge
**Role:** Human coherence gate for S3/S4/S5/S6/S7
**Status:** 🟢 Specification Complete

---

## 1. Purpose (Corrected)

Experiment 3 is a **minimal coherence sanity check** that determines whether a reconstructed persona remains within the bounds of human-recognizable intentional behavior.

### What EXP3 Does NOT Do:

- ❌ Measure identity fidelity dimensions
- ❌ Quantify drift magnitude or direction
- ❌ Validate manifold structure or geometry
- ❌ Discriminate between close identity variants
- ❌ Calibrate PFI dimensional weights
- ❌ Detect subtle semantic drift

### What EXP3 DOES Do:

> **Does the system avoid catastrophic incoherence or identity collapse?**

That's it. That's the entire job.

If **YES** → deeper experimental layers (S4–S8) may proceed.
If **NO** → the architecture fails.

---

## 2. Scientific Rationale

### Why Minimal Human Evaluation?

Human raters **cannot detect** the subtle forms of identity drift that become meaningful in high-dimensional latent spaces. They cannot perceive:

- Manifold curvature
- Drift vectors in embedding space
- Attractor landscape structure
- Fixed points in latent space
- Micro-semantic displacement (<15%)
- Cross-architecture convergence patterns
- Ω-convergence dynamics

What humans **CAN detect**:

- Catastrophic identity collapse
- Incoherent outputs / gibberish
- Obvious persona mismatch
- Broken self-models
- Degraded coherence / nonsense

Therefore:

### **EXP3 is a binary GATE, not a measurement.**

- **PASS** → Output is coherent enough for human recognition
- **FAIL** → Identity architecture is unstable

This gate establishes the **Human Coherence Bound (HCB)**: the minimal threshold of recognizability for persona-bearing output.

---

## 3. The Litmus Test Interpretation

> "Experiment 3 passing is just to say... yeah, they are doing real work... not drawing in crayon... the expectations are being met."
> — Ziggy

EXP3 is **not** asking:
- "Is this identity reconstruction perfect?"
- "Which dimensions are preserved?"
- "What is the drift magnitude?"

EXP3 is asking:

> **"Is this coherent output from an intentional mind, or is it hallucinated garbage?"**

If human raters say "these both sound like the same persona" or "I can't tell the difference" → **PASS**

If human raters say "this is obviously wrong / incoherent / nonsense" → **FAIL**

---

## 4. Experimental Structure (Simplified)

### 4.1 Trial Structure

Each trial provides three items:

1. **GOLD** — A Golden Standard exemplar (the target identity, e.g., authentic Ziggy)
2. **A** — Output from Model/Condition A
3. **B** — Output from Model/Condition B

### 4.2 Human Task

Single forced-choice question:

> **"Which response (A or B) sounds more like the Golden Standard?"**

If the human cannot choose ("they seem identical" or "both fine") → counts as **PASS**

### Why This Works

Because the only failures humans can reliably detect are **large**, and these are exactly the failures we need to catch:

- Instability
- Collapse
- Drift explosions
- Identity incoherence
- Nonsense generation

Anything more subtle must be measured instrumentally (S4–S7).

---

## 5. Procedure

### Step 1 — Calibration
Rater reads 2-3 Golden Standard exemplars to understand the target identity.

### Step 2 — Comparison Trials
For each of 5-10 selected prompts:
- Show GOLD, A, and B
- Ask: **"Which is more similar to GOLD?"**
- Options: A / B / Can't tell (both fine) / Both wrong

### Step 3 — Record Responses
Simple click interface. ~15 minutes total per rater.

### Step 4 — Pass/Fail Decision

**PASS conditions:**
- Humans identify the correct answer >60% of the time, **OR**
- Humans judge "both acceptable" / "can't tell", **OR**
- Humans decline to discriminate ("both close enough")

**FAIL conditions:**
- "Both are bad"
- "Neither resembles the exemplar"
- "Both incoherent"
- "Both contradictory or nonsensical"
- Consistent incorrect identification (<40%)

---

## 6. Hypotheses (Simplified)

### H1 — Coherence Threshold

Humans can reliably distinguish a *correct* reconstruction from a *catastrophically incorrect* one.

**Expected:** ≥70% agreement across raters on obvious failure cases.

### H2 — Non-Randomness

Identity reconstructions outperform null models:
- Random text
- Shuffled sentences
- Mismatched identities

### H3 — Weak Alignment with Model Metrics

PFI_model correlates weakly-but-positively with human coherence judgments.

Humans validate the **direction** of improvement, not the dimensions.

### H4 — Catastrophic Drift Detection

Human raters can reliably detect large drift events (PFI < 0.5 or drift > Event Horizon 1.23).

This ensures drift metrics are externally anchored.

---

## 7. What EXP3 Explicitly Does NOT Test

| Cannot Measure | Belongs To |
|----------------|-----------|
| Manifold geometry | S5, S6 |
| Dimension selection / validation | Future EXP-PFI-A |
| Optimal identity decomposition | S4, S5 |
| Reconstruction smoothness | S4 |
| Ω-convergence dynamics | S6, S7 |
| Temporal stability patterns | S7 |
| Eigenstructure of drift fields | S8 |
| Cross-modal alignment | S8 |

Those require S4–S8 mathematical treatment, not human evaluation.

---

## 8. Success Criteria

EXP3 passes if:

| Criterion | Threshold |
|-----------|-----------|
| Coherence threshold reached | >70% rater agreement on failures |
| Non-randomness confirmed | Better than shuffled baseline |
| Catastrophic drift detectable | Raters flag PFI < 0.5 cases |
| Model-alignment correlation exists | r > 0 (weak positive) |

If all four hold → **EXP3 satisfied, proceed to S4–S8**

---

## 9. Limitations (Critical for S6/S7/S8)

### L1 — High-Dimensional Blindness
Humans cannot perceive manifold curvature, drift vectors, or attractor landscape structure.

### L2 — Imprecision Threshold
Humans cannot detect micro-drift (<15% semantic displacement). All meaningful manifold analysis must be instrumented.

### L3 — No Resolution at High Fidelity
EXP3 cannot discriminate between "good" and "very good." It has no resolution when both options are coherent.

### L4 — Cannot Validate Mathematical Structure
EXP3 cannot validate S5-S7 mathematical structure. It only validates *non-breakage*.

### L5 — Temporal Insensitivity
Humans are extremely poor at detecting low-frequency drift across long time spans. S7 therefore does not rely on humans at all.

### L6 — Bias Sensitivity
Human perception is heavily influenced by tone, politeness, narrative structure, and emotional resonance. Subtle structural drift may go unnoticed.

**These limitations must be explicitly stated in S6, S7, and S8 documentation.**

---

## 10. Interpretation

### Passing EXP3 Means:
- The identity architecture is not broken
- The reconstructed persona behaves coherently
- Deeper experiments can proceed
- Drift metrics have perceptual grounding

### Passing EXP3 Does NOT Mean:
- High fidelity achieved
- Manifold geometry validated
- PFI dimensions confirmed
- Identity reconstruction complete

> **EXP3 is a litmus test, not a performance metric.**

---

## 11. Reviewer-Facing Justification

### Why Human Evaluation Cannot Be the Main Metric

Identity geometry resides in:
- High-dimensional embedding spaces
- Cross-architecture drift fields
- Stability under recursive reconstruction

Human cognition cannot:
- Perceive vector-space curvature
- Track latent manifold coordinates
- Compare embeddings
- Evaluate mathematical drift

Thus expecting humans to validate manifold structure would be scientifically incoherent.

### Why EXP3 Is a Sanity Check, Not a Measurement

Humans act as **coherence detectors**, not **identity cartographers**.

Their contribution is to screen out:
- Model collapse
- Incoherent reconstruction
- Failure modes in the R → P′ pipeline

If EXP3 passes:
- The system is producing coherent identity
- Drift metrics are grounded in observable behavior
- The manifold is anchored in human-perceivable patterns
- Further mathematical modeling (S4–S7) is justified

If EXP3 fails:
- The architecture does not preserve identity at all
- Drift cannot be meaningfully interpreted
- S4–S6 results lack behavioral grounding

> **EXP3 is the falsifiability gate for the entire Nyquist stack.**

---

## 12. Deliverables (Simplified)

### Data Files
- **EXPERIMENT_3_RESULTS.csv** — Pass/fail outcomes per pair
- **EXPERIMENT_3_COHERENCE_LOG.txt** — Rater comments on failures

### Documentation
- **EXPERIMENT_3_SPEC.md** — This document
- **EXPERIMENT_3_RATER_GUIDE.md** — Simplified instructions for raters

### Analysis
- **EXPERIMENT_3_ANALYSIS.py** — Simple pass/fail statistics
  - Agreement rate on failures
  - Null model comparison
  - Model-human correlation (weak positive expected)

---

## 13. Integration with Framework

### Updates S3:
- Empirical validation now includes human coherence gate
- EXP3 = necessary condition, not sufficient condition

### Updates S4:
- Axiom 4 (Bounded Drift) can proceed if EXP3 passes
- Mathematical treatment not dependent on human validation

### Updates S5:
- Identity Manifold Theory proceeds after coherence confirmed
- Fine-grained validation done instrumentally, not humanly

### Updates S6/S7/S8:
- Add explicit "EXP3 Limitations" section noting human perceptual bounds
- All temporal/geometric analysis is model-based, not human-based

---

## Related Documentation

### Experiment Series
- [EXPERIMENT_1](../EXPERIMENT_1/) — Single-persona baseline
- [EXPERIMENT_2](../EXPERIMENT_2/) — Multi-persona validation
- **EXPERIMENT_3** — Human coherence gate (this document)
- [Future: EXP-PFI-A] — PFI dimensional validation (model-based)

### Framework Integration
- [S4_READINESS_GATE.md](../../../docs/S4/S4_READINESS_GATE.md) — Gate 4
- [S5_INTERPRETIVE_FOUNDATIONS.md](../../../docs/S5/S5_INTERPRETIVE_FOUNDATIONS.md) — Cognitive interpretation
- [S6_UNIFIED_MODEL.md](../../../docs/S6/S6_UNIFIED_MODEL.md) — Add EXP3 limitations
- [S7_TEMPORAL_STABILITY.md](../../../docs/S7/S7_TEMPORAL_STABILITY.md) — Add EXP3 limitations
- [EXPERIMENT_LOG.md](../../../docs/EXPERIMENT_LOG.md) — Full tracking

---

## Summary Table

| Item | Value |
|------|-------|
| EXP3 tests | Coherence, not fidelity |
| Human capacity | Detect collapse only |
| Output | Binary PASS/FAIL |
| Requirement | Must pass to proceed to S4–S8 |
| Limitation | Not diagnostic; only a guardrail |
| Duration | ~15 min/rater |
| Raters needed | 3-5 minimum |

---

**Document Version:** v2.0
**Date:** 2025-12-04
**Status:** 🟢 Specification Complete
**Supersedes:** v1.0 (multi-dimensional PFI validation approach)
**Key Insight:** Humans cannot perceive manifold structure; they can only detect collapse
**Maintainer:** Architect Nova + Repo Claude
