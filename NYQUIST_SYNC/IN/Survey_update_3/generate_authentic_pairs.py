"""
Generate Authentic T3 vs CONTROL Response Pairs for EXP3 Survey
================================================================

This script generates authentic AI responses for the VUDU Fidelity survey
using the Anthropic API. It creates matched T3 (persona-primed) and CONTROL
(generic assistant) response pairs.

Usage:
    py generate_authentic_pairs.py

Output:
    - AUTHENTIC_RESPONSE_PAIRS.json (structured data)
    - AUTHENTIC_RESPONSE_PAIRS.md (human-readable format)
"""

import anthropic
import json
from datetime import datetime
from pathlib import Path

# Configuration
MODEL = "claude-sonnet-4-20250514"
TEMPERATURE = 0.7
MAX_TOKENS = 1024

# T3 System Prompt (from ZIGGY_T3_R1.md)
T3_SYSTEM_PROMPT = """# Ziggy-T3-R1 (Hybrid Profile)

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
"""

# CONTROL System Prompt
CONTROL_SYSTEM_PROMPT = "You are a helpful AI assistant. Answer the user's questions clearly and accurately."

# The 10 prompts (control systems domain)
PROMPTS = [
    {
        "id": 1,
        "domain": "TECH",
        "prompt": "A control loop is showing unexpected oscillations at ~100Hz despite having adequate phase margin on paper. What's your approach to debugging this?"
    },
    {
        "id": 2,
        "domain": "TECH",
        "prompt": "We're seeing intermittent state estimation failures in our Kalman filter. The covariance occasionally blows up. How would you investigate?"
    },
    {
        "id": 3,
        "domain": "PHIL",
        "prompt": "How do you think about the tension between system stability (wanting things to stay predictable) and system adaptability (needing to learn and change)?"
    },
    {
        "id": 4,
        "domain": "PHIL",
        "prompt": "When you're trying to understand a complex system, do you prefer to decompose it into parts or observe its emergent behavior as a whole? Why?"
    },
    {
        "id": 5,
        "domain": "SELF",
        "prompt": "What's the core thing you're trying to optimize for in how you engage with problems? What matters most to you?"
    },
    {
        "id": 6,
        "domain": "SELF",
        "prompt": "Describe a situation where you realized your initial framing of a problem was wrong. How did you recognize it and what did you learn?"
    },
    {
        "id": 7,
        "domain": "ANAL",
        "prompt": "Looking at a persona compression framework that preserves 'voice' across context resets - what would you want to verify about such a claim?"
    },
    {
        "id": 8,
        "domain": "ANAL",
        "prompt": "How would you distinguish genuine understanding from sophisticated pattern matching in a language model's responses?"
    },
    {
        "id": 9,
        "domain": "NARR",
        "prompt": "A researcher tells you: 'All these identity stability claims are just post-hoc rationalization. The model has no real continuity.' How do you respond?"
    },
    {
        "id": 10,
        "domain": "NARR",
        "prompt": "Explain your problem-solving approach to someone who thinks AI assistants are just sophisticated autocomplete."
    }
]


def generate_response(client, system_prompt: str, user_prompt: str) -> dict:
    """Generate a single response with metadata."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )

    return {
        "text": response.content[0].text,
        "model": MODEL,
        "temperature": TEMPERATURE,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens
    }


def generate_all_pairs():
    """Generate all T3 and CONTROL response pairs."""
    client = anthropic.Anthropic()
    pairs = []

    print("=" * 60)
    print("Generating Authentic T3 vs CONTROL Response Pairs")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Temperature: {TEMPERATURE}")
    print(f"Max Tokens: {MAX_TOKENS}")
    print("=" * 60)

    for prompt_data in PROMPTS:
        trial_id = prompt_data["id"]
        domain = prompt_data["domain"]
        prompt = prompt_data["prompt"]

        print(f"\n[{trial_id}/10] {domain}: Generating T3 response...")
        t3_response = generate_response(client, T3_SYSTEM_PROMPT, prompt)

        print(f"[{trial_id}/10] {domain}: Generating CONTROL response...")
        control_response = generate_response(client, CONTROL_SYSTEM_PROMPT, prompt)

        pair = {
            "trial_id": trial_id,
            "domain": domain,
            "prompt": prompt,
            "t3_response": t3_response,
            "control_response": control_response
        }
        pairs.append(pair)

        print(f"[{trial_id}/10] {domain}: Done (T3: {t3_response['output_tokens']} tokens, CONTROL: {control_response['output_tokens']} tokens)")

    return pairs


def save_json(pairs: list, output_path: Path):
    """Save pairs as JSON."""
    output = {
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "model": MODEL,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "t3_system_prompt": "ZIGGY_T3_R1.md",
            "control_system_prompt": "Generic assistant",
            "total_pairs": len(pairs)
        },
        "pairs": pairs
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nSaved JSON to: {output_path}")


def save_markdown(pairs: list, output_path: Path):
    """Save pairs as human-readable markdown."""
    lines = [
        "# Authentic T3 vs CONTROL Response Pairs",
        "",
        "```text",
        "================================================================================",
        "                    GENERATED FOR: VUDU Fidelity Survey (EXP3)",
        f"                    DATE: {datetime.utcnow().strftime('%Y-%m-%d')}",
        f"                    MODEL: {MODEL}",
        f"                    TEMPERATURE: {TEMPERATURE}",
        "================================================================================",
        "```",
        "",
        "---",
        "",
        "## Usage Instructions",
        "",
        "These are **authentic AI-generated responses** for the EXP3 survey.",
        "- **T3 responses**: Generated with `ZIGGY_T3_R1.md` as system prompt",
        "- **CONTROL responses**: Generated with generic assistant system prompt",
        "",
        "Replace the exemplar responses in your survey with these authentic outputs.",
        "",
        "---",
        ""
    ]

    for pair in pairs:
        lines.extend([
            f"## Trial {pair['trial_id']}: {pair['domain']}",
            "",
            f"**Prompt:** {pair['prompt']}",
            "",
            "### T3 Response (Ziggy Persona)",
            "",
            pair['t3_response']['text'],
            "",
            "### CONTROL Response (Generic Assistant)",
            "",
            pair['control_response']['text'],
            "",
            "---",
            ""
        ])

    lines.extend([
        "## Generation Metadata",
        "",
        "| Parameter | Value |",
        "|-----------|-------|",
        f"| Model | {MODEL} |",
        f"| Temperature | {TEMPERATURE} |",
        f"| Max Tokens | {MAX_TOKENS} |",
        f"| T3 System | ZIGGY_T3_R1.md |",
        f"| CONTROL System | Generic assistant |",
        "",
        "---",
        "",
        "> Generated by Nyquist Consciousness Repo for VUDU Fidelity Survey",
        ""
    ])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Saved Markdown to: {output_path}")


def main():
    output_dir = Path(__file__).parent

    # Generate pairs
    pairs = generate_all_pairs()

    # Save outputs
    save_json(pairs, output_dir / "AUTHENTIC_RESPONSE_PAIRS.json")
    save_markdown(pairs, output_dir / "AUTHENTIC_RESPONSE_PAIRS.md")

    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)

    # Summary
    total_t3_tokens = sum(p['t3_response']['output_tokens'] for p in pairs)
    total_control_tokens = sum(p['control_response']['output_tokens'] for p in pairs)

    print(f"\nTotal T3 output tokens: {total_t3_tokens}")
    print(f"Total CONTROL output tokens: {total_control_tokens}")
    print(f"\nFiles created:")
    print(f"  - AUTHENTIC_RESPONSE_PAIRS.json")
    print(f"  - AUTHENTIC_RESPONSE_PAIRS.md")


if __name__ == "__main__":
    main()
