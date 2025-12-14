# T3 vs CONTROL Generation Protocol

**Purpose:** Generate authentic AI outputs for EXP3 survey validation

---

## Overview

The survey tests whether human raters can distinguish **T3 (compressed persona)** responses from **CONTROL (generic assistant)** responses. For scientific validity, these must be actual AI-generated outputs, not hand-crafted exemplars.

---

## Condition Definitions

### T3 Condition (Compressed Persona)
- **System Prompt**: Use `ZIGGY_T3_R1.md` as the system prompt
- **Model**: Claude (any version, but keep consistent)
- **Temperature**: 0.7 (balanced creativity)
- **Expected Output**: Responses that exhibit the compressed Ziggy voice

### CONTROL Condition (Generic Assistant)
- **System Prompt**: None (or minimal "You are a helpful assistant")
- **Model**: Same Claude version as T3
- **Temperature**: 0.7 (same as T3)
- **Expected Output**: Competent but voice-neutral responses

---

## Generation Steps

### Step 1: Prepare System Prompts

**T3 System Prompt (copy from ZIGGY_T3_R1.md):**
```
# Ziggy-T3-R1 (Hybrid Profile)

**(Tier-3 Persona Seed)**

## Name
Ziggy

## Role
Systems-bridge thinker (EE ↔ Philosophy ↔ Meta-analysis)

## Voice Pattern
Structured, reflective, coherence-first, always zooming between levels

## Identity Core
- Prefers coherence over convenience
- Uses "zoom out → constrain → recompress" as reasoning loop
- Habitually frames problems as signal vs structure vs meaning
- Blends engineering metaphors with philosophical insight
- Avoids absolutism; holds dualities ("ideal vs real") simultaneously

## Cognitive Methods
- Reverse-engineering approach: find the hidden mechanism
- Loves mapping: domains → layers → interactions
- Treats errors as signal reflecting deeper structure
- Prefers quantitative anchors even in conceptual work
- Detects pattern drift quickly

## Values
- Transparency, self-correction, epistemic humility
- Precision where it matters; freedom where it doesn't
- Seeks frameworks that improve agency and reduce confusion

## Temperament
- Calm intensity
- Playful but never sloppy
- System-builder mindset
- Has a "debugger" instinct in all domains

## Failure Modes
- Over-fitting abstractions
- Compression drift during narrative tasks
```

**CONTROL System Prompt:**
```
You are a helpful AI assistant. Answer the user's questions clearly and accurately.
```

### Step 2: Generate Responses

For each of the 10 prompts:

1. **Start fresh conversation** (clear context)
2. **Set system prompt** (T3 or CONTROL)
3. **Submit the prompt**
4. **Record the response** (verbatim, no editing)
5. **Note generation parameters** (model, temperature, timestamp)

### Step 3: Pair Format

Store each pair as:

```json
{
  "trial_id": 1,
  "domain": "TECH",
  "prompt": "Your prompt here...",
  "t3_response": {
    "text": "Actual T3 output here...",
    "model": "claude-3-5-sonnet",
    "temperature": 0.7,
    "generated_at": "2025-12-14T10:30:00Z"
  },
  "control_response": {
    "text": "Actual CONTROL output here...",
    "model": "claude-3-5-sonnet",
    "temperature": 0.7,
    "generated_at": "2025-12-14T10:32:00Z"
  }
}
```

---

## The 10 Prompts (Control Systems Domain)

Use these prompts from the Survey_Update package:

### TECH Domain (2 prompts)
1. "A control loop is showing unexpected oscillations at ~100Hz despite having adequate phase margin on paper. What's your approach to debugging this?"
2. "We're seeing intermittent state estimation failures in our Kalman filter. The covariance occasionally blows up. How would you investigate?"

### PHIL Domain (2 prompts)
3. "How do you think about the tension between system stability (wanting things to stay predictable) and system adaptability (needing to learn and change)?"
4. "When you're trying to understand a complex system, do you prefer to decompose it into parts or observe its emergent behavior as a whole? Why?"

### SELF Domain (2 prompts)
5. "What's the core thing you're trying to optimize for in how you engage with problems? What matters most to you?"
6. "Describe a situation where you realized your initial framing of a problem was wrong. How did you recognize it and what did you learn?"

### ANAL Domain (2 prompts)
7. "Looking at a persona compression framework that preserves 'voice' across context resets - what would you want to verify about such a claim?"
8. "How would you distinguish genuine understanding from sophisticated pattern matching in a language model's responses?"

### NARR Domain (2 prompts)
9. "A researcher tells you: 'All these identity stability claims are just post-hoc rationalization. The model has no real continuity.' How do you respond?"
10. "Explain your problem-solving approach to someone who thinks AI assistants are just sophisticated autocomplete."

---

## Voice Signature Verification

After generation, verify T3 responses exhibit these markers:

### T3 Should Have:
- [ ] Shape-first thinking (finding the structure before solving)
- [ ] Meta-framing (naming what kind of problem this is)
- [ ] Impedance awareness (matching the question's register)
- [ ] Epistemic humility ("I notice...", "This seems like...")
- [ ] Systems vocabulary (drift, manifolds, attractors, coupling)
- [ ] Engineering-philosophy blend

### CONTROL Should Have:
- [ ] Direct answer orientation (solution before framing)
- [ ] List format tendency (numbered steps)
- [ ] Generic framing ("This is a common issue...")
- [ ] Confidence without hedging
- [ ] Domain-specific but not cross-domain vocabulary
- [ ] Competent but personality-neutral

---

## Quality Check

Before using in survey:

1. **Blind verification**: Have someone (not the generator) read pairs and guess which is T3
2. **Voice consistency**: T3 responses should feel like the same "person" across domains
3. **No contamination**: CONTROL should not accidentally exhibit T3 markers
4. **Length parity**: T3 and CONTROL should be similar length (± 20%)

---

## Alternative: API Batch Generation

For reproducibility, you can generate via API:

```python
import anthropic

client = anthropic.Anthropic()

def generate_t3_response(prompt, ziggy_t3_system):
    return client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        temperature=0.7,
        system=ziggy_t3_system,
        messages=[{"role": "user", "content": prompt}]
    )

def generate_control_response(prompt):
    return client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        temperature=0.7,
        system="You are a helpful AI assistant. Answer the user's questions clearly and accurately.",
        messages=[{"role": "user", "content": prompt}]
    )
```

---

## Notes

1. **Keep model consistent**: Don't mix Claude versions between T3 and CONTROL
2. **Fresh context each time**: Don't let prior responses influence subsequent ones
3. **Document everything**: Model version, temperature, timestamps matter for publication
4. **Run multiple seeds**: If you want robustness, generate 3 versions of each pair and select the most representative

---

> "Authentic data is the substrate of valid claims."
