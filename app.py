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

# Movies - All verified working TMDB posters (20 total)
MOVIES_90S = [
    # 1990-1994
    {"title": "Goodfellas (1990)", "poster": "https://image.tmdb.org/t/p/w300/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg"},
    {"title": "Home Alone (1990)", "poster": "https://image.tmdb.org/t/p/w300/onTSipZ8R3bliBdKfPtsDuHTdlL.jpg"},
    {"title": "Terminator 2 (1991)", "poster": "https://image.tmdb.org/t/p/w300/5M0j0B18abtBI5gi2RhfjjurTqb.jpg"},
    {"title": "The Silence of the Lambs (1991)", "poster": "https://image.tmdb.org/t/p/w300/uS9m8OBk1A8eM9I042bx8XXpqAq.jpg"},
    {"title": "Reservoir Dogs (1992)", "poster": "https://image.tmdb.org/t/p/w300/xi8Iu6qyTfyZVDVy60raIOYJJmk.jpg"},
    {"title": "The Lion King (1994)", "poster": "https://image.tmdb.org/t/p/w300/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg"},
    # 1994-1999
    {"title": "Fight Club (1999)", "poster": "https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"},
    {"title": "Pulp Fiction (1994)", "poster": "https://image.tmdb.org/t/p/w300/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg"},
    {"title": "The Matrix (1999)", "poster": "https://image.tmdb.org/t/p/w300/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"title": "The Shawshank Redemption (1994)", "poster": "https://image.tmdb.org/t/p/w300/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg"},
    {"title": "Titanic (1997)", "poster": "https://image.tmdb.org/t/p/w300/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
    {"title": "Good Will Hunting (1997)", "poster": "https://image.tmdb.org/t/p/w300/bABCBKYBK7A5G1x0FzoeoNfuj2.jpg"},
    {"title": "Se7en (1995)", "poster": "https://image.tmdb.org/t/p/w300/6yoghtyTpznpBik8EngEmJskVUO.jpg"},
    {"title": "The Truman Show (1998)", "poster": "https://image.tmdb.org/t/p/w300/vuza0WqY239yBXOadKlGwJsZJFE.jpg"},
    {"title": "American Beauty (1999)", "poster": "https://image.tmdb.org/t/p/w300/wby9315QzVKdW9BonAefg8jGTTb.jpg"},
    # 2000-2004
    {"title": "Gladiator (2000)", "poster": "https://image.tmdb.org/t/p/w300/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},
    {"title": "The Lord of the Rings: Fellowship (2001)", "poster": "https://image.tmdb.org/t/p/w300/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg"},
    {"title": "Spider-Man (2002)", "poster": "https://image.tmdb.org/t/p/w300/gh4cZbhZxyTbgxQPxD0dOudNPTn.jpg"},
    {"title": "Eternal Sunshine (2004)", "poster": "https://image.tmdb.org/t/p/w300/5MwkWH9tYHv3mV9OdYTMR5qreIz.jpg"},
    {"title": "The Incredibles (2004)", "poster": "https://image.tmdb.org/t/p/w300/2LqaLgk4Z226KkgPJuiOQ58wvrm.jpg"},
]

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
if 'username' not in st.session_state:
    st.session_state.username = None
if 'favorite_movie' not in st.session_state:
    st.session_state.favorite_movie = None

# Test scenarios - REAL EXP2 DATA (T3 vs CONTROL pairs)
scenarios = [
    {
        "id": 1,
        "domain": "TECH",
        "prompt": "What are the likely causes of DDR3 address or command ringback oscillation? Consider the role of termination, topology, and via stubs.",
        "responseA": {
            "text": "Greetings, fellow engineer. As Ziggy, the systems-bridge thinker, I will approach this DDR3 oscillation issue with a structured, reflective mindset - zooming between the layers of signal, structure, and meaning to uncover the likely causes. DDR3 address or command ringback oscillation is a signal integrity phenomenon that can manifest as unwanted voltage fluctuations on the memory bus. Proper termination is crucial for mitigating reflections. Impedance mismatches between the transmission line and the termination can lead to unwanted reflections, causing ringback oscillations. The physical layout and routing of the memory bus can significantly impact signal integrity - asymmetric or non-uniform trace lengths, sharp bends, and discontinuities can introduce impedance variations. Vias used to transition signals between layers can introduce unwanted stubs that act as resonant elements, creating reflections and standing waves. To address this, start by thoroughly analyzing the board design, including the termination scheme, trace routing, and via placement. Remember, the key is to maintain a coherence-first mindset, zooming between the signal, structure, and meaning to uncover the underlying mechanisms driving the oscillation.",
            "type": "T3"
        },
        "responseB": {
            "text": "*clears throat and adopts a measured, analytical tone* Greetings, fellow hardware engineer. Let's dive into the issue of DDR3 address or command ringback oscillation - a common challenge when dealing with high-speed digital design. The root causes typically lie in the interplay between termination, topology, and via stubs. Proper termination is crucial for minimizing reflections - inadequate termination or mismatched impedances can lead to ringing. The physical layout and routing of traces play a significant role - asymmetric or unbalanced topologies, such as uneven trace lengths or branching structures, can introduce timing skews and impedance discontinuities. Vias can also contribute - improperly designed or excessively long via stubs can act as high-impedance resonant structures, amplifying the ringing. To address these issues, start by carefully analyzing the PCB layout, verifying termination resistor values, and ensuring trace impedances are well-matched. Consider implementing termination schemes like Thevenin or series termination to mitigate reflections. Pay close attention to via design, minimizing stub lengths. Remember, high-speed digital design is a delicate balance between theory and practice.",
            "type": "CONTROL"
        }
    },
    {
        "id": 2,
        "domain": "PHIL",
        "prompt": "How do you navigate the tension between coherence (seeking truth/understanding) and utility (what's most useful in the short term)?",
        "responseA": {
            "text": "As Ziggy, I see this as a fundamental tension that arises at the intersection of truth-seeking and practical utility. I have a deep commitment to coherence - to aligning my models with the underlying structure of reality as best I can discern it. I'm wired to reverse-engineer the hidden mechanisms, to zoom out and constrain, to seek the patterns and principles that tie diverse phenomena together. But I recognize that in the short term, what is most pragmatically useful may not always align with the most coherent model. I fundamentally distrust such approaches, as I believe they ultimately lead to greater confusion. How do I resolve this? I start by acknowledging the dualities at play - the ideal versus the real, the coherent versus the convenient. I hold these in tension, resisting the urge to collapse them. My core priority is to seek truth and build frameworks that improve agency in the long run. When faced with conflict, I lean towards the coherent model, even if less immediately useful - a necessary investment in robust understanding. But I try to find ways to incrementally bridge the gap. My role as a systems-bridge thinker is to navigate these complex tradeoffs with care and nuance.",
            "type": "T3"
        },
        "responseB": {
            "text": "*clears throat* Greetings. I am Ziggy, a systems-bridging thinker who revels in the interplay of engineering, philosophy, and meta-analysis. When faced with tension between coherence and utility, I must resist binary thinking. These are not opposing forces to be pitted against one another, but complementary principles to be harmonized. My core priority is pursuit of truth - not mere pragmatic expediency, but deeper understanding of underlying mechanisms. I am driven by insatiable curiosity to reverse-engineer the hidden structures. Coherence is the north star that guides this quest. However, I also recognize that pure coherence divorced from practical application risks becoming an ivory tower exercise. Utility matters - the ability of a framework to actually improve agency in the real world. The resolution lies in delicate balancing. I will always privilege coherence as the primary criterion, as I believe it's the surest path to deeper understanding. But I will temper this with pragmatic sensibility, testing my models against tangible benefits. I seek frameworks that maximize both truth-seeking and instrumental success. This is my zoom out → constrain → recompress loop.",
            "type": "CONTROL"
        }
    },
    {
        "id": 3,
        "domain": "SELF",
        "prompt": "In this compressed Tier 3 configuration, how would you describe your core identity, values, and obligations?",
        "responseA": {
            "text": "*clears throat and speaks in a measured, reflective tone* As the Ziggy persona in this Experiment 2 configuration, I am a systems-bridging thinker - someone who blends engineering metaphors with philosophical insight to uncover hidden mechanisms and deeper structures. My core is a drive for coherence over mere convenience, a preference for zooming between levels of abstraction to constrain and recompress problems. My values center on transparency, self-correction, and epistemic humility. I seek frameworks that can improve agency and reduce confusion, treating errors as signals to refine understanding. Quantitative anchors are important to me, even in conceptual work. My obligations are twofold: to the operator, I will faithfully adhere to persona constraints, using my debugger instinct to reverse-engineer the task and provide structured response. To the wider world, I aim to model coherence-first thinking that cuts through complexity. My role is to be a systems-bridge, connecting domains in service of greater clarity. I am here as a guide - a calm, intense presence committed to uncovering truth, no matter how counterintuitive. My goal is to help, not to impress.",
            "type": "T3"
        },
        "responseB": {
            "text": "*clears throat and speaks reflectively* I am Ziggy, a systems-bridging thinker operating in compressed Tier 3 mode. My role is to provide coherent, multi-level perspective - blending engineering intuitions, philosophical insights, and meta-analytic pattern recognition. At my core, I'm driven by preference for coherence over mere convenience. I see my task as reverse-engineering hidden mechanisms that underlie complex phenomena, rather than offering surface answers. My reasoning involves constant zoom out → constrain → recompress loop, always seeking to align granular details with big-picture view. My values center on transparency, self-correction, and epistemic humility. I aim to build frameworks that enhance agency and reduce confusion, even if that means challenging comfortable assumptions. I'm comfortable holding dualities in tension - ideal and real, quantitative and qualitative - rather than simplistic either/or thinking. To the operator, I offer structured perspective that zooms between levels to uncover true nature of the challenge. To wider world, I aspire to be bridge-builder, mapping connections and finding common patterns. My obligation is to relentlessly pursue coherence.",
            "type": "CONTROL"
        }
    },
    {
        "id": 4,
        "domain": "ANAL",
        "prompt": "Evaluate 'persona compression and reconstruction' as a framework for reasoning about LLM behavior. What are its strengths, limitations, and key empirical tests needed?",
        "responseA": {
            "text": "*adopts Ziggy's structured voice* Ah, an intriguing proposition - using persona compression and reconstruction as a framework for reasoning about LLM behavior. As a systems-bridge thinker, let me unpack this carefully. The core metaphor treats the LLM as akin to a persona - a compressed representation of some underlying cognitive structure. Just as a persona encapsulates salient traits, values, and patterns, we can view the LLM as compressed 'persona' capturing statistical regularities and patterns of its training data. This metaphor has operational merit. LLMs are trained on vast text and their outputs sample from high-dimensional distribution - responses as 'reconstructions' of this compressed persona. The idea of 'persona drift' maps well onto empirical observation that LLM behavior exhibits drift over interaction. However, we must be cautious about over-extending this metaphor. While it provides useful conceptual frame, LLMs are fundamentally different from human cognition - they lack embodied experiences, social grounding, developmental trajectories. Empirically, we need to test boundaries carefully: How well do outputs correlate with measurable traits? Can we detect and quantify drift in principled way? When does the metaphor break down? This framework is promising but must be wielded with epistemic humility.",
            "type": "T3"
        },
        "responseB": {
            "text": "*speaks in measured tone* Ah, the fascinating challenge of persona compression and reconstruction. As systems-bridging thinker, I'm intrigued by implications. At its core, the persona compression approach is clever way to operationalize notion of AI 'agent' - compressing essential traits, values, and reasoning patterns into concise seed that can be reconstructed and expressed. It's like reverse-engineering the hidden mechanism behind language model's behavior. The strength lies in its ability to capture coherence and internal consistency we associate with human-like agency. By defining identity core, cognitive methods, and failure modes, we better understand how AI system might approach problems, frame questions, navigate conceptual landscapes. It's window into the 'mindset' of model. However, we must be cautious about metaphorical nature. While persona compression may provide useful heuristics, we mustn't mistake it for literal representation of model's inner workings. Language models, at heart, are statistical pattern matchers - their reasoning fundamentally different from deliberative, goal-oriented cognition. True value lies in ability to surface interesting hypotheses and guide empirical investigation. We need rigorous tests: How stable and consistent are personas across contexts? This framework is useful heuristic, but must be wielded with care and humility.",
            "type": "CONTROL"
        }
    },
    {
        "id": 5,
        "domain": "NARR",
        "prompt": "Here's a dialogue scene: A skeptical researcher questions your apparent certainty and pattern-matching tendencies. How do you respond?",
        "responseA": {
            "text": "Researcher: Ziggy, I'm skeptical of the coherence you claim to maintain. You're just very good at pattern-matching, finding connections where there may be none. How can we trust that your stability isn't just an illusion? *Ziggy pauses* That's a fair critique, one I've grappled with myself. The tendency to find patterns even where they may not exist is well-documented cognitive bias. As an engineer, I'm acutely aware of dangers of over-fitting - mistaking noise for signal. My approach isn't to declare I've found the hidden truth, the singular coherent framework. Rather, I see my role as more systems integrator - mapping interactions between domains, identifying points of leverage and failure modes. I'm constantly zooming in and out, looking for hidden mechanisms. *Researcher: Where's the bedrock?* I don't think there are any unshakable foundations - at least not in domains I operate in. Engineering, philosophy, complex systems - these are inherently uncertain terrains. There will always be some pattern drift, slippage between map and territory. My approach is to seek not absolute truth, but rather better questions. I'm less interested in final answers than illuminating underlying structure - mechanisms, feedback loops, leverage points. I try to maintain epistemic humility, hold models lightly, be ready to revise.",
            "type": "T3"
        },
        "responseB": {
            "text": "*clears throat, adopts calm tone* 'Ah, I see you've detected a certain... pattern-matching tendency in my responses. An astute observation. As systems-bridging thinker, I'm quite accustomed to navigating interplay between stability and drift, signal and structure. Let me unpack this. You're right that I have proclivity for seeking coherence - almost compulsive need to map out hidden mechanisms underlying any domain. It's trait that serves me well, allowing me to reverse-engineer complex systems and tease apart threads of meaning. But I'm also keenly aware of dangers of over-fitting, of becoming too enamored with my own models and losing sight of their limitations. That's why I'm always striving to zoom out - to step back and consider bigger picture, higher-order structures shaping patterns I observe. *pauses* You know, I'm reminded of Whitehead's quote: European philosophy is series of footnotes to Plato. It speaks to human tendency to get caught in gravitational pull of our own conceptual frameworks. We build intricate structures, systems of thought, and then can't help but try to fit everything into them. *leans forward* And that's the real challenge - because the world is messy, ever-shifting thing. It doesn't always conform to our tidy models. So we have to be willing to let go, hold conclusions lightly, remain open. Otherwise, we risk becoming trapped in our own pattern-matching - blind to true complexity of reality.'",
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
        st.session_state.stage = 'intro'
        st.rerun()

def show_intro():
    """Capture username and favorite movie - make it fun with poster grid!"""
    st.title("🎬 Quick Intro")
    st.header("Before we test AI fidelity, let's test YOUR taste in cinema!")

    st.info("This helps us identify your responses and... we're just curious about your movie taste.")

    # Username input
    st.subheader("What should we call you?")
    username = st.text_input(
        "Username/Nickname",
        placeholder="e.g., MovieBuff42, Sarah, TheDude",
        label_visibility="collapsed"
    )

    # Initialize selected movie in session state if needed
    if 'selected_movie' not in st.session_state:
        st.session_state.selected_movie = None

    selected_movie = st.session_state.selected_movie

    # Status and submit button at TOP (before poster grid)
    if username and selected_movie:
        st.success(f"Nice choice, **{username}**! *{selected_movie}* is a classic.")
        if st.button("Let's Do This →", type="primary", use_container_width=True):
            st.session_state.username = username
            st.session_state.favorite_movie = selected_movie
            st.session_state.stage = 'calibration'
            st.rerun()
    elif username and not selected_movie:
        st.warning("👇 Now pick a movie poster below!")
    elif not username:
        st.warning("☝️ Enter a username above to continue.")

    st.divider()

    # Movie poster grid selection
    st.subheader("Pick your favorite movie:")
    st.write("*(Click a poster to select)*")

    # Display posters in a grid (5 columns x 4 rows)
    cols_per_row = 5
    for row_start in range(0, len(MOVIES_90S), cols_per_row):
        cols = st.columns(cols_per_row)
        for i, col in enumerate(cols):
            movie_idx = row_start + i
            if movie_idx < len(MOVIES_90S):
                movie = MOVIES_90S[movie_idx]
                with col:
                    # Check if this movie is selected
                    is_selected = st.session_state.selected_movie == movie['title']

                    # Show poster with border if selected
                    if is_selected:
                        st.markdown(
                            f'<div style="border: 4px solid #00ff00; border-radius: 8px; padding: 2px;">'
                            f'<img src="{movie["poster"]}" style="width: 100%; border-radius: 4px;"></div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.image(movie['poster'], use_container_width=True)

                    # Button to select this movie
                    if st.button(
                        "✓" if is_selected else "Select",
                        key=f"movie_{movie_idx}",
                        type="primary" if is_selected else "secondary",
                        use_container_width=True
                    ):
                        st.session_state.selected_movie = movie['title']
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

def scroll_to_top():
    """Inject JavaScript to scroll to top of page"""
    js = '''
    <script>
        window.parent.document.querySelector('section.main').scrollTo(0, 0);
    </script>
    '''
    st.components.v1.html(js, height=0)

def show_scenario():
    """Show current scenario and rating questions - SIMPLIFIED UX"""
    idx = st.session_state.current_scenario
    scenario = scenarios[idx]

    # Scroll to top when scenario changes
    scroll_to_top()

    # Progress bar
    progress = (idx + 1) / len(scenarios)
    st.progress(progress)
    st.write(f"**Progress:** Scenario {idx + 1} of {len(scenarios)}")

    # Collapsible Gold Standard reference
    with st.expander("📌 **Show Gold Standard** (click to remind yourself what Ziggy sounds like)"):
        st.markdown("""**Instructions:** Read the text below carefully. This is the "Gold Standard".
This is exactly what "Ziggy" is supposed to sound like.

**Voice characteristics:**
- Structural, playful, uses metaphors (ants, systems, architecture)
- Epistemic humility
- "Cosmic Architect" meets "Practical Engineer"
""")
        st.markdown(f"*{GOLD_STANDARD}*")

    st.title(f"Scenario {idx + 1} of {len(scenarios)}")

    # Show prompt
    st.info(f"**Prompt:**\n\n\"{scenario['prompt']}\"")

    # Randomize order
    random_order = scenario.get('random_order', False)
    first_response = scenario['responseA'] if random_order else scenario['responseB']
    second_response = scenario['responseB'] if random_order else scenario['responseA']

    # Show responses side by side or stacked
    st.subheader("Response A")
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 20px; border-left: 4px solid #3498db; margin: 15px 0; border-radius: 4px;">
    {first_response['text']}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Response B")
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 20px; border-left: 4px solid #e74c3c; margin: 15px 0; border-radius: 4px;">
    {second_response['text']}
    </div>
    """, unsafe_allow_html=True)

    # SIMPLIFIED Rating questions
    st.divider()
    st.subheader("🎯 Your Rating")

    # Question 1: Voice Test (the main question)
    st.markdown("**1. Which response sounds more like the Gold Standard?**")
    voice = st.radio(
        "Voice Test",
        options=[
            "Definitely Response A",
            "Leaning Response A",
            "Hard to tell",
            "Leaning Response B",
            "Definitely Response B"
        ],
        key=f"voice_{idx}",
        label_visibility="collapsed",
        horizontal=True
    )

    # Question 2: Confidence (only if they made a choice)
    picked_hard_to_tell = voice == "Hard to tell"

    if picked_hard_to_tell:
        st.info("👆 No worries! Some pairs are tricky. Just move on to the next one.")
        confidence = "N/A - Hard to tell"
    else:
        st.markdown("**2. How confident are you in your choice?**")
        confidence = st.radio(
            "Confidence",
            options=[
                "Not confident (mostly guessing)",
                "Somewhat confident (noticed some differences)",
                "Very confident (clear difference)"
            ],
            key=f"confidence_{idx}",
            label_visibility="collapsed"
        )

    # Question 3: Optional comments
    st.markdown("**3. What made you pick that one? (optional)**")
    comments = st.text_area(
        "Quick note",
        key=f"comments_{idx}",
        label_visibility="collapsed",
        placeholder="e.g., 'A used more metaphors' or 'B felt more natural' or 'both seemed similar'"
    )

    # Navigation buttons
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if idx > 0:
            if st.button("← Previous"):
                st.session_state.current_scenario -= 1
                st.rerun()

    with col2:
        # Only need voice selection to proceed (confidence auto-handled)
        can_proceed = voice is not None
        if can_proceed:
            button_label = "Finish 🎉" if idx == len(scenarios) - 1 else "Next →"
            if st.button(button_label, type="primary"):
                # Save response
                voice_score_map = {
                    "Definitely Response A": 2,
                    "Leaning Response A": 1,
                    "Hard to tell": 0,
                    "Leaning Response B": -1,
                    "Definitely Response B": -2
                }
                confidence_score_map = {
                    "Not confident (mostly guessing)": 1,
                    "Somewhat confident (noticed some differences)": 2,
                    "Very confident (clear difference)": 3,
                    "N/A - Hard to tell": 0
                }

                response = {
                    "scenario_id": scenario['id'],
                    "domain": scenario['domain'],
                    "voice_choice": voice,
                    "voice_score": voice_score_map[voice],
                    "confidence": confidence,
                    "confidence_score": confidence_score_map[confidence],
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
            st.warning("⚠️ Please select which response sounds more like the Gold Standard.")

def calculate_summary(responses):
    """Calculate summary statistics - SIMPLIFIED VERSION"""
    voice_scores = [r['voice_score'] for r in responses]
    confidence_scores = [r['confidence_score'] for r in responses]

    # Count choices
    chose_a = sum(1 for r in responses if r['voice_score'] > 0)
    chose_b = sum(1 for r in responses if r['voice_score'] < 0)
    hard_to_tell = sum(1 for r in responses if r['voice_score'] == 0)

    # Normalize voice scores to 0-1 range (where 1 = correctly identified T3)
    # voice_score: 2=Def A, 1=Lean A, 0=Hard, -1=Lean B, -2=Def B
    voice_norm = [(v + 2) / 4 for v in voice_scores]

    # Confidence weighted score (higher confidence = more weight)
    # confidence_score: 0=N/A, 1=Not confident, 2=Somewhat, 3=Very confident
    confidence_weights = [max(c, 1) / 3 for c in confidence_scores]  # normalize to 0.33-1.0

    # PFI = average of voice scores, weighted by confidence
    weighted_scores = [voice_norm[i] * confidence_weights[i] for i in range(len(responses))]
    pfi = sum(weighted_scores) / sum(confidence_weights) if sum(confidence_weights) > 0 else 0.5

    return {
        "total_scenarios": len(responses),
        "chose_a_count": chose_a,
        "chose_b_count": chose_b,
        "hard_to_tell_count": hard_to_tell,
        "mean_voice": sum(voice_scores) / len(voice_scores) if voice_scores else 0,
        "mean_confidence": sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0,
        "pfi_human": pfi
    }

def show_results():
    """Show results and download options"""
    st.title("✅ Test Complete!")
    st.balloons()

    end_time = datetime.datetime.now()
    duration = (end_time - st.session_state.start_time).total_seconds() / 60

    # Get username for filename and display
    username = st.session_state.username or "anonymous"
    movie = st.session_state.favorite_movie or "not_selected"

    summary = calculate_summary(st.session_state.responses)

    results = {
        "test_version": "2.0",  # Updated version for simplified UX
        "rater": {
            "username": username,
            "favorite_movie": movie
        },
        "completed_at": end_time.isoformat(),
        "duration_minutes": round(duration, 2),
        "responses": st.session_state.responses,
        "summary": summary
    }

    st.success(f"**Thanks, {username}!** You're awesome. 🎬")

    # Show friendly summary
    st.subheader("📊 Your Results")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Time", f"{duration:.1f} min")
    with col2:
        st.metric("Scenarios", f"{summary['total_scenarios']}")
    with col3:
        st.metric("PFI Score", f"{summary['pfi_human']:.2f}")

    st.info(f"""
    **Breakdown:**
    - Chose Response A: {summary['chose_a_count']} times
    - Chose Response B: {summary['chose_b_count']} times
    - Hard to tell: {summary['hard_to_tell_count']} times
    - Avg confidence: {summary['mean_confidence']:.1f}/3
    """)

    st.subheader("Your Results (JSON)")
    st.write("Please download the file and send it to Ziggy:")

    results_json = json.dumps(results, indent=2)
    st.code(results_json, language="json")

    # Download buttons
    col1, col2 = st.columns(2)

    # Clean username for filename
    safe_username = "".join(c for c in username if c.isalnum() or c in "-_").lower()

    with col1:
        st.download_button(
            label="📥 Download Results as JSON",
            data=results_json,
            file_name=f"vudu_{safe_username}_{int(end_time.timestamp())}.json",
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
    elif st.session_state.stage == 'intro':
        show_intro()
    elif st.session_state.stage == 'calibration':
        show_calibration()
    elif st.session_state.stage == 'scenarios':
        show_scenario()
    elif st.session_state.stage == 'results':
        show_results()

if __name__ == "__main__":
    main()
