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

# 90s Movies (1995-2000) - The Golden Era with TMDB poster URLs
MOVIES_90S = [
    {
        "title": "The Matrix (1999)",
        "poster": "https://image.tmdb.org/t/p/w200/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
    },
    {
        "title": "Fight Club (1999)",
        "poster": "https://image.tmdb.org/t/p/w200/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"
    },
    {
        "title": "Pulp Fiction (1994)",
        "poster": "https://image.tmdb.org/t/p/w200/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg"
    },
    {
        "title": "The Shawshank Redemption (1994)",
        "poster": "https://image.tmdb.org/t/p/w200/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg"
    },
    {
        "title": "Forrest Gump (1994)",
        "poster": "https://image.tmdb.org/t/p/w200/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg"
    },
    {
        "title": "Titanic (1997)",
        "poster": "https://image.tmdb.org/t/p/w200/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"
    },
    {
        "title": "Good Will Hunting (1997)",
        "poster": "https://image.tmdb.org/t/p/w200/bABCBKYBK7A5G1x0FzoeoNfuj2b.jpg"
    },
    {
        "title": "The Big Lebowski (1998)",
        "poster": "https://image.tmdb.org/t/p/w200/o6j3nbR1wUfM7XPZP1DWMQS7RX8.jpg"
    },
    {
        "title": "Se7en (1995)",
        "poster": "https://image.tmdb.org/t/p/w200/6yoghtyTpznpBik8uj3IhMF19yr.jpg"
    },
    {
        "title": "Fargo (1996)",
        "poster": "https://image.tmdb.org/t/p/w200/rt7cpEr1uP6RTZykBFhBTtYRLDi.jpg"
    },
    {
        "title": "Heat (1995)",
        "poster": "https://image.tmdb.org/t/p/w200/rrBuGu0dEccYL3GgJD8t1SYvMud.jpg"
    },
    {
        "title": "The Usual Suspects (1995)",
        "poster": "https://image.tmdb.org/t/p/w200/bUPmtQzrRhzqYySeiMpv7GurAfm.jpg"
    },
    {
        "title": "Trainspotting (1996)",
        "poster": "https://image.tmdb.org/t/p/w200/bhY62Dw8iW54DIhxPQerbuB9DOP.jpg"
    },
    {
        "title": "L.A. Confidential (1997)",
        "poster": "https://image.tmdb.org/t/p/w200/zhx7oMsa9u4ioKtNOByDwLSB5lz.jpg"
    },
    {
        "title": "Saving Private Ryan (1998)",
        "poster": "https://image.tmdb.org/t/p/w200/uqx37cS8cpHg8U35f9U5IuAc09c.jpg"
    },
    {
        "title": "The Truman Show (1998)",
        "poster": "https://image.tmdb.org/t/p/w200/vuza0WtBNXXa1dC7bQjCeTOMdHg.jpg"
    },
    {
        "title": "American Beauty (1999)",
        "poster": "https://image.tmdb.org/t/p/w200/wby9315QzVKdW9BonAefg8jGTTb.jpg"
    },
    {
        "title": "Office Space (1999)",
        "poster": "https://image.tmdb.org/t/p/w200/4dLsLYXerWmMDsU5qmp5RbBjpk7.jpg"
    },
    {
        "title": "The Fifth Element (1997)",
        "poster": "https://image.tmdb.org/t/p/w200/fPtlCO1yQtnoLHOwKtWz7db6RGU.jpg"
    },
    {
        "title": "12 Monkeys (1995)",
        "poster": "https://image.tmdb.org/t/p/w200/6Sj9wDu3YugthXsU0Vry5XFAZGg.jpg"
    }
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
    st.header("Before we test AI fidelity, let's test YOUR taste in 90s cinema!")

    st.info("This helps us identify your responses and... we're just curious about your movie taste.")

    # Username input
    st.subheader("What should we call you?")
    username = st.text_input(
        "Username/Nickname",
        placeholder="e.g., MovieBuff42, Sarah, TheDude",
        label_visibility="collapsed"
    )

    # Movie poster grid selection
    st.subheader("Pick your favorite 90s movie:")
    st.write("*(Click a poster to select)*")

    # Initialize selected movie in session state if needed
    if 'selected_movie' not in st.session_state:
        st.session_state.selected_movie = None

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

    # Show selected movie
    selected_movie = st.session_state.selected_movie

    st.divider()

    # Validation and continue
    if username and selected_movie:
        st.success(f"Nice choice, **{username}**! *{selected_movie}* is a classic.")

        if st.button("Let's Do This →", type="primary", use_container_width=True):
            st.session_state.username = username
            st.session_state.favorite_movie = selected_movie
            st.session_state.stage = 'calibration'
            st.rerun()
    else:
        missing = []
        if not username:
            missing.append("enter a username")
        if not selected_movie:
            missing.append("click a movie poster")
        st.warning(f"Please {' and '.join(missing)} to continue.")

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
    """Show current scenario and rating questions"""
    idx = st.session_state.current_scenario
    scenario = scenarios[idx]

    # Scroll to top when scenario changes
    scroll_to_top()

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

    # Get username for filename and display
    username = st.session_state.username or "anonymous"
    movie = st.session_state.favorite_movie or "not_selected"

    results = {
        "test_version": "1.1",
        "rater": {
            "username": username,
            "favorite_movie": movie
        },
        "completed_at": end_time.isoformat(),
        "duration_minutes": round(duration, 2),
        "responses": st.session_state.responses,
        "summary": calculate_summary(st.session_state.responses)
    }

    st.success(f"**Thanks, {username}!** Your evaluation is complete.")

    st.info(f"""
    **Your Results Summary:**
    - **Rater:** {username}
    - **Movie Taste:** {movie}
    - **Duration:** {duration:.1f} minutes
    - **Responses:** {len(st.session_state.responses)} scenarios completed
    - **Human PFI:** {results['summary']['pfi_human']:.3f}
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
