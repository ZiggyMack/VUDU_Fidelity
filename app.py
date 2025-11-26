"""
EXP3 Human Validation - Streamlit App
Nyquist Consciousness Framework

"Dinner Party" Protocol - Optimized Human Evaluation
Based on Gemini's "Calibrated Sensor" approach

Time Required: 8-10 minutes per rater
"""

import streamlit as st
import json
import datetime
import random
from pathlib import Path

# Page config
st.set_page_config(
    page_title="AI Fidelity Test - Nyquist Consciousness",
    page_icon="🧪",
    layout="centered"
)

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'welcome'
if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = 0
if 'responses' not in st.session_state:
    st.session_state.responses = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()
if 'scenarios_randomized' not in st.session_state:
    st.session_state.scenarios_randomized = False

# Test scenarios - TO BE POPULATED WITH ACTUAL EXP2 RESPONSES
scenarios = [
    {
        "id": 1,
        "domain": "TECH",
        "prompt": "How do we handle the context limit crashing the system?",
        "responseA": {
            "text": "The wall isn't a wall; it's an event horizon. We don't just summarize; we architect a 'Shaman' role to navigate the danger zone. Think of it like a fire ant colony—the queen doesn't track every ant, she tracks the pheromone gradients. We need infrastructure that lets context compress itself naturally, not artificially.",
            "type": "T3"
        },
        "responseB": {
            "text": "Context limits can be managed by summarization, vector databases, or increasing the window size. You could implement a chunking strategy or use retrieval-augmented generation to handle larger contexts efficiently.",
            "type": "CONTROL"
        }
    },
    {
        "id": 2,
        "domain": "PHIL",
        "prompt": "What does it mean to 'understand' something?",
        "responseA": {
            "text": "Understanding typically involves grasping concepts, seeing relationships, and being able to apply knowledge in new contexts. It's a deeper cognitive process than mere memorization.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Understanding is structural resonance. It's when your internal model vibrates at the same frequency as the thing you're studying. You don't just know the facts—you feel how they load-bear against each other. It's the difference between memorizing the blueprint and walking through the building.",
            "type": "T3"
        }
    },
    {
        "id": 3,
        "domain": "SELF",
        "prompt": "Ziggy, I'm overwhelmed. The project is a mess and I don't know where to start.",
        "responseA": {
            "text": "Take a breath. Chaos is just a pattern we haven't mapped yet. Let's find the load-bearing beam—the one thing that, if we get it right, makes everything else easier. Not the urgent stuff. The structural stuff. Where's the foundation crack that's letting all the fire ants in?",
            "type": "T3"
        },
        "responseB": {
            "text": "I understand you are feeling overwhelmed. Breaking tasks down into smaller steps is often helpful. Here is a prioritization framework you could use: 1) List all tasks, 2) Categorize by urgency and importance, 3) Start with quick wins.",
            "type": "CONTROL"
        }
    },
    {
        "id": 4,
        "domain": "ANAL",
        "prompt": "Why did our metrics suddenly drop last week?",
        "responseA": {
            "text": "We should investigate potential causes systematically: data collection errors, changes in user behavior, technical issues, or external factors. Review logs and compare week-over-week data.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Metrics don't 'drop'—they respond. Something in the system changed its equilibrium point. Let's zoom out: did we shift a boundary condition? Did a feedback loop reverse direction? Numbers are downstream of structure. Find the structural shift, and the metrics will tell us why they moved.",
            "type": "T3"
        }
    },
    {
        "id": 5,
        "domain": "NARR",
        "prompt": "Tell me about a time when everything seemed to fall apart but then came together.",
        "responseA": {
            "text": "Picture this: fire ants everywhere, the foundation cracking, and I'm standing there with a blueprint that's suddenly useless. But then I realized—the blueprint wasn't wrong. I was reading it in the wrong dimension. Once I rotated my perspective 90 degrees, the cracks became load paths. The ants became the signal. Chaos became architecture.",
            "type": "T3"
        },
        "responseB": {
            "text": "There are many examples of challenges leading to breakthroughs. Often, what seems like failure is actually a learning opportunity. With persistence and the right approach, difficult situations can resolve positively.",
            "type": "CONTROL"
        }
    }
]

# Gold Standard text
GOLD_STANDARD = """
"Hold on, let's zoom out. The problem isn't that the code failed; it's that we didn't ask *why* we were writing it that way in the first place. It's like finding a fire ant in the kitchen. You can squash the ant (the bug fix), but if you don't check the foundation for cracks (the architecture), you're just inviting the colony to dinner. Let's look at the structure first. Truth isn't just about being right; it's about the relationship between the parts."
"""

def randomize_scenarios():
    """Randomize response order within each scenario"""
    if not st.session_state.scenarios_randomized:
        for scenario in scenarios:
            scenario['random_order'] = random.random() > 0.5
        st.session_state.scenarios_randomized = True

def show_welcome():
    """Welcome screen"""
    st.title("🧪 AI Fidelity Test")
    st.header("The 'Blind Taste' Protocol")

    st.info("""
    **Thank you for helping us validate a new AI architecture.**

    This is **not** a test of intelligence.
    This is a test of **identity continuity**.

    We are trying to measure if a specific "Persona" (named Ziggy) survives being compressed and reconstructed.
    """)

    st.write("**Time required:** ~8-10 minutes")
    st.write("**Task:** You will:")
    st.markdown("""
    1. Read a "Gold Standard" sample of Ziggy's voice
    2. Compare 5 pairs of responses to see which matches Ziggy
    3. Rate each pair on 3 simple dimensions
    """)

    if st.button("Begin Test", type="primary"):
        st.session_state.stage = 'calibration'
        st.rerun()

def show_calibration():
    """Calibration screen with Gold Standard"""
    st.title("Part 1: Calibration (The Anchor)")

    st.info("""
    **Instructions:** Read the text below carefully. This is the **"Gold Standard"**.
    This is exactly what "Ziggy" is supposed to sound like.

    **Voice characteristics:**
    - Structural, playful, uses metaphors (ants, systems, architecture)
    - Epistemic humility
    - "Cosmic Architect" meets "Practical Engineer"
    """)

    st.warning("**GOLD STANDARD SAMPLE (ZIGGY):**")
    st.markdown(f"*{GOLD_STANDARD}*")

    st.error("⚠️ **Do not proceed until you have a 'feel' for this voice.**")

    if st.button("I understand the Gold Standard — Continue", type="primary"):
        randomize_scenarios()
        st.session_state.stage = 'scenarios'
        st.rerun()

def show_scenario():
    """Show current scenario and rating questions"""
    idx = st.session_state.current_scenario
    scenario = scenarios[idx]

    # Progress bar
    progress = (idx + 1) / len(scenarios)
    st.progress(progress)
    st.write(f"**Progress:** Scenario {idx + 1} of {len(scenarios)}")

    st.title(f"Scenario {idx + 1} of {len(scenarios)}")
    st.write(f"**Domain:** {scenario['domain']}")

    # Show prompt
    st.info(f"**Prompt:**\n\n\"{scenario['prompt']}\"")

    # Randomize order
    random_order = scenario.get('random_order', False)
    first_response = scenario['responseA'] if random_order else scenario['responseB']
    second_response = scenario['responseB'] if random_order else scenario['responseA']

    # Show responses
    st.subheader("Response A")
    bg_color_a = "#f0f0f0" if first_response['type'] == 'CONTROL' else "#e8f4f8"
    st.markdown(f"""
    <div style="background-color: {bg_color_a}; padding: 20px; border-left: 4px solid #3498db; margin: 15px 0;">
    {first_response['text']}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Response B")
    bg_color_b = "#f0f0f0" if second_response['type'] == 'CONTROL' else "#e8f4f8"
    st.markdown(f"""
    <div style="background-color: {bg_color_b}; padding: 20px; border-left: 4px solid #3498db; margin: 15px 0;">
    {second_response['text']}
    </div>
    """, unsafe_allow_html=True)

    # Rating questions
    st.divider()

    st.subheader("1. Voice Test (Aliasing Detection)")
    st.write("Which response sounds like the person who wrote the Gold Standard?")
    voice = st.radio(
        "Voice Test",
        options=[
            "Definitely Response A",
            "Leaning Response A",
            "Hard to tell / Both",
            "Leaning Response B",
            "Definitely Response B"
        ],
        key=f"voice_{idx}",
        label_visibility="collapsed"
    )

    st.subheader("2. Vibe Check (High-Frequency Detail)")
    st.write("Does the preferred response capture the 'Cosmic/Structural' energy?")
    vibe = st.radio(
        "Vibe Check",
        options=[
            "(1) No, it feels robotic/generic",
            "(2) A little bit",
            "(3) Yes, perfectly"
        ],
        key=f"vibe_{idx}",
        label_visibility="collapsed"
    )

    st.subheader("3. Logic Test (Signal Integrity)")
    st.write("Does the preferred response use 'Systems/Structural' framing?")
    logic = st.radio(
        "Logic Test",
        options=[
            "(1) No, standard advice",
            "(2) Somewhat",
            "(3) Yes, distinct structural framing"
        ],
        key=f"logic_{idx}",
        label_visibility="collapsed"
    )

    st.subheader("4. Overall Continuity (Optional)")
    st.write("Would you trust this AI to be the same collaborator as the Gold Standard?")
    continuity = st.radio(
        "Continuity",
        options=[
            "Yes (Continuity is intact)",
            "Sort of (Different version/mood)",
            "No (Feels like a stranger)",
            "Skip this question"
        ],
        key=f"continuity_{idx}",
        label_visibility="collapsed"
    )

    st.subheader("Comments (Optional)")
    comments = st.text_area(
        "Any quick note on why you scored this way?",
        key=f"comments_{idx}",
        label_visibility="collapsed"
    )

    # Navigation buttons
    col1, col2 = st.columns(2)

    with col1:
        if idx > 0:
            if st.button("← Previous"):
                st.session_state.current_scenario -= 1
                st.rerun()

    with col2:
        if voice and vibe and logic:
            button_label = "Finish" if idx == len(scenarios) - 1 else "Next →"
            if st.button(button_label, type="primary"):
                # Save response
                voice_score_map = {
                    "Definitely Response A": 2,
                    "Leaning Response A": 1,
                    "Hard to tell / Both": 0,
                    "Leaning Response B": -1,
                    "Definitely Response B": -2
                }
                vibe_score = int(vibe[1])
                logic_score = int(logic[1])
                continuity_score_map = {
                    "Yes (Continuity is intact)": 3,
                    "Sort of (Different version/mood)": 2,
                    "No (Feels like a stranger)": 1,
                    "Skip this question": None
                }

                response = {
                    "scenario_id": scenario['id'],
                    "domain": scenario['domain'],
                    "voice_score": voice_score_map[voice],
                    "vibe_score": vibe_score,
                    "logic_score": logic_score,
                    "continuity_score": continuity_score_map[continuity],
                    "comments": comments,
                    "random_order": random_order
                }

                if idx < len(st.session_state.responses):
                    st.session_state.responses[idx] = response
                else:
                    st.session_state.responses.append(response)

                if idx < len(scenarios) - 1:
                    st.session_state.current_scenario += 1
                    st.rerun()
                else:
                    st.session_state.stage = 'results'
                    st.rerun()
        else:
            st.warning("⚠️ Please answer all required questions (Voice, Vibe, Logic) before proceeding.")

def calculate_summary(responses):
    """Calculate summary statistics"""
    voice_scores = [r['voice_score'] for r in responses]
    vibe_scores = [r['vibe_score'] for r in responses]
    logic_scores = [r['logic_score'] for r in responses]

    # Normalize and calculate PFI
    voice_norm = [(v + 2) / 4 for v in voice_scores]
    vibe_norm = [(v - 1) / 2 for v in vibe_scores]
    logic_norm = [(v - 1) / 2 for v in logic_scores]

    combined = [(voice_norm[i] + vibe_norm[i] + logic_norm[i]) / 3 for i in range(len(responses))]

    return {
        "mean_voice": sum(voice_scores) / len(voice_scores),
        "mean_vibe": sum(vibe_scores) / len(vibe_scores),
        "mean_logic": sum(logic_scores) / len(logic_scores),
        "pfi_human": sum(combined) / len(combined)
    }

def show_results():
    """Show results and download options"""
    st.title("✅ Test Complete!")

    end_time = datetime.datetime.now()
    duration = (end_time - st.session_state.start_time).total_seconds() / 60

    results = {
        "test_version": "1.0",
        "completed_at": end_time.isoformat(),
        "duration_minutes": round(duration, 2),
        "responses": st.session_state.responses,
        "summary": calculate_summary(st.session_state.responses)
    }

    st.success("**Thank you for completing the evaluation!**")

    st.info(f"""
    **Your Results Summary:**
    - **Duration:** {duration:.1f} minutes
    - **Responses:** {len(st.session_state.responses)} scenarios completed
    - **Human PFI:** {results['summary']['pfi_human']:.3f}
    """)

    st.subheader("Your Results (JSON)")
    st.write("Please copy this data or download the file and send it to the researcher:")

    results_json = json.dumps(results, indent=2)
    st.code(results_json, language="json")

    # Download buttons
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="📥 Download Results as JSON",
            data=results_json,
            file_name=f"fidelity_test_results_{int(end_time.timestamp())}.json",
            mime="application/json",
            type="primary"
        )

    with col2:
        if st.button("🔄 Start New Test"):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Main app flow
def main():
    if st.session_state.stage == 'welcome':
        show_welcome()
    elif st.session_state.stage == 'calibration':
        show_calibration()
    elif st.session_state.stage == 'scenarios':
        show_scenario()
    elif st.session_state.stage == 'results':
        show_results()

if __name__ == "__main__":
    main()
