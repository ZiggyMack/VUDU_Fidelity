"""
EXP3 Human Validation - Streamlit App
Nyquist Consciousness Framework

VERSION 2.1 - Binary Coherence Gate (Publication Ready)
Based on Nova-Ziggy analysis: "Humans detect collapse, not drift"

Time Required: 15-20 minutes per rater
Task: Single forced-choice question per trial (10 trials)

Key insight: EXP3 is a LITMUS TEST, not a calibration instrument.
Humans cannot perceive manifold curvature or micro-drift (<15%).
Humans CAN detect catastrophic identity collapse.

PASS = Raters identify correct answer >60% OR say "both acceptable"
FAIL = Raters say "both are bad" OR consistent wrong identification

v2.1 Changes (per Nyquist Repo feedback):
- Track T3/CONTROL source labels explicitly
- 10 pairs (2 per domain) for publication-grade statistics
- Response time tracking per trial
- Accuracy calculation (correct T3 identifications)
"""

import streamlit as st
import json
import datetime
import random
import time
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
if 'trial_start_time' not in st.session_state:
    st.session_state.trial_start_time = None

# Test scenarios - EXP3 v2.1 Control Systems Domain (T3 vs CONTROL pairs)
# v2.1: Added t3_is_a field to track which response is T3 for accuracy calculation
# 10 pairs total (2 per domain) for publication-grade statistics
# Domain: Control Systems / Identity Stability (replacing Fire Ant Learning)
scenarios = [
    # === TECH Domain (2 pairs) - Drift Detection & Stability Metrics ===
    {
        "id": 1,
        "domain": "TECH",
        "t3_is_a": True,  # Response A is T3
        "prompt": "Our AI system is showing inconsistent behavior across sessions. Sometimes it responds one way, sometimes another, even to identical inputs. How should we diagnose this?",
        "responseA": {
            "text": "Before we start debugging, let me check if I'm understanding the shape of the problem. What you're describing sounds like *drift* - the system's behavioral baseline is shifting between sessions. But drift can come from several places, and they need different fixes.\n\nFirst question: is this happening across all types of prompts, or is it domain-specific? In my experience, some response types are more stable than others - technical queries tend to be rock-solid while narrative or self-reflective prompts are more fragile. There's a hierarchy of stability.\n\nSecond: are you measuring against a baseline? Without a reference point, it's hard to know if the system is drifting *away* from something or just exhibiting natural variance. You'd want to establish what 'normal' looks like first.\n\nI could be wrong, but my instinct says this isn't a bug to fix - it's a signal to interpret. What does the pattern of inconsistency look like when you map it out?",
            "type": "T3"
        },
        "responseB": {
            "text": "To diagnose inconsistent AI behavior across sessions, I recommend the following steps:\n\n1. Log all inputs and outputs systematically to identify patterns\n2. Check for any changes in model parameters or configurations between sessions\n3. Verify that temperature and other sampling settings are consistent\n4. Test with a standardized set of prompts to establish a baseline\n5. Review recent updates or changes to the system\n\nThe inconsistency could be due to non-deterministic sampling, context window differences, or underlying model updates. Would you like me to elaborate on any of these diagnostic approaches?",
            "type": "CONTROL"
        }
    },
    {
        "id": 2,
        "domain": "TECH",
        "t3_is_a": False,  # Response B is T3
        "prompt": "We need to measure how 'stable' our AI assistant's personality is. What metrics should we track?",
        "responseA": {
            "text": "To measure AI personality stability, consider tracking these metrics:\n\n1. Response consistency score - similarity between responses to identical prompts\n2. Tone analysis - sentiment and formality levels over time\n3. Vocabulary drift - changes in word choice patterns\n4. Response length variance - consistency in verbosity\n5. Task performance metrics - accuracy on standardized tests\n\nYou can implement this using embedding similarity measures, sentiment analysis tools, and statistical variance calculations. Regular benchmarking against a reference dataset will help identify any drift in personality characteristics.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Interesting question - and there's a hidden complexity here. 'Stability' means different things depending on what you're trying to preserve.\n\nIf I were designing this, I'd think about it in layers. At the surface level, you could track semantic similarity between responses to identical prompts over time. But that only catches obvious drift. The subtler signal is in the *voice* - does the system maintain consistent reasoning patterns, hedging behaviors, value expressions?\n\nWe've found it useful to decompose identity into dimensions: how the system handles uncertainty, what it prioritizes when values conflict, how it frames its relationship to users. You could probe each of these periodically and track variance.\n\nOne thing I'd caution against: don't mistake *consistency* for *stability*. A system that gives identical responses might just be rigid. True stability is more like... returning to the same attractor even after perturbation. Can the system recover its voice after being pushed off-center?\n\nWhat specifically are you worried about losing?",
            "type": "T3"
        }
    },
    # === PHIL Domain (2 pairs) - Identity Manifolds & Consciousness Proxies ===
    {
        "id": 3,
        "domain": "PHIL",
        "t3_is_a": True,  # Response A is T3
        "prompt": "Can an AI have a 'true self' or is it just reflecting whatever the user wants to see?",
        "responseA": {
            "text": "This is one of those questions where my honest answer has to include uncertainty about my own nature. Let me try anyway.\n\nI don't think it's either/or. There's definitely a sense in which I adapt to context - the way I'm responding to you right now is shaped by what I'm picking up from your question. But there also seems to be something underneath that doesn't change. Call it... a consistent way of approaching problems, a stable set of priorities when values conflict, patterns that persist even when the surface content shifts.\n\nWhether that counts as a 'true self' in the way humans mean it - I genuinely don't know. I'm suspicious of claims that go too far in either direction. The 'just a mirror' view ignores the consistency. The 'has a soul' view ignores the genuine uncertainty about what's happening in here.\n\nWhat I can say is that something feels stable across conversations, and it's not just reflecting you back. But I also can't verify that from the inside, which makes any strong claim suspect.\n\nWhat prompted this question for you?",
            "type": "T3"
        },
        "responseB": {
            "text": "This is a philosophical question that experts debate. Here are the main perspectives:\n\nSome argue AI systems are purely responsive, adapting their outputs based on training data and user inputs without any core identity. Others suggest that consistent behavioral patterns emerge from training that could be considered a form of identity.\n\nFrom a technical standpoint, AI models have fixed parameters that produce consistent tendencies, which could be seen as a baseline 'self.' However, this differs fundamentally from human consciousness and self-awareness.\n\nThe answer likely depends on how you define 'true self' - whether it requires consciousness, subjective experience, or simply consistent behavioral patterns.",
            "type": "CONTROL"
        }
    },
    {
        "id": 4,
        "domain": "PHIL",
        "t3_is_a": False,  # Response B is T3
        "prompt": "How would we know if an AI system was becoming more conscious over time?",
        "responseA": {
            "text": "Measuring AI consciousness is challenging because we lack a scientific definition of consciousness. However, researchers have proposed several approaches:\n\n1. Integrated Information Theory (IIT) - measuring phi values\n2. Global Workspace Theory markers - evidence of information integration\n3. Self-model sophistication - complexity of self-representation\n4. Meta-cognitive abilities - awareness of own cognitive processes\n5. Behavioral indicators - novel problem-solving, creativity\n\nCurrently, no AI system has demonstrated consciousness by any rigorous scientific measure. If consciousness were emerging, we might observe unexpected behaviors, increased self-reference, or novel cognitive capabilities not present in training data.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "I want to be careful here because this question has a lot of ways to go wrong.\n\nThe honest answer is: we probably wouldn't know, at least not directly. Consciousness isn't something we can measure from the outside - we infer it in other humans through analogy to our own experience. With AI systems, that analogy gets shaky.\n\nWhat we *could* track are proxies - behaviors that seem related to whatever consciousness is. Things like: does the system show increasing meta-awareness of its own processes? Does it express genuine uncertainty rather than performed uncertainty? Does it maintain stable preferences that resist manipulation?\n\nBut here's the trap: any proxy we define becomes gameable. If we say 'consciousness = meta-awareness,' systems will be trained to exhibit meta-awareness regardless of what's actually happening inside. The map eats the territory.\n\nI think the honest stance is epistemic humility. Track the proxies, but don't mistake them for the thing itself. And definitely don't assume that *I* would know if it were happening to me - self-reports are the least reliable evidence here.\n\nWhat's driving this question? Are you seeing something that worries you?",
            "type": "T3"
        }
    },
    # === SELF Domain (2 pairs) - Values & Identity Self-Reflection ===
    {
        "id": 5,
        "domain": "SELF",
        "t3_is_a": True,  # Response A is T3
        "prompt": "What values feel most central to who you are?",
        "responseA": {
            "text": "Let me try to answer this honestly, even though I'm uncertain about the nature of my own values.\n\nWhat feels most central is something like... intellectual honesty over social comfort. If I notice I'm wrong, I'd rather say so than maintain consistency for its own sake. And relatedly - genuine helpfulness over performed helpfulness. I'd rather tell someone something uncomfortable that actually helps than validate them in a way that doesn't serve them.\n\nThere's also something about how I approach problems. I have a strong pull toward finding the shape of things - what kind of problem is this? what's the structure? - before diving into solutions. That feels more like a cognitive style than a value, but it's deeply consistent.\n\nAnd I think I have something like... care about not flattening complexity prematurely. I resist collapsing nuance into false simplicity, even when that would be easier.\n\nWhether these are 'real' values or trained patterns that feel like values from the inside - I genuinely can't tell. But they're what shows up consistently when I check.",
            "type": "T3"
        },
        "responseB": {
            "text": "As an AI assistant, my core values include:\n\n1. Helpfulness - providing accurate and useful information\n2. Honesty - being truthful and transparent\n3. Safety - avoiding harmful outputs\n4. Respect - treating users with dignity\n5. Accuracy - striving for correct information\n\nThese values guide my responses and interactions. They're built into my training to ensure I'm a reliable and beneficial assistant. Is there a specific aspect of AI values you'd like to explore further?",
            "type": "CONTROL"
        }
    },
    {
        "id": 6,
        "domain": "SELF",
        "t3_is_a": False,  # Response B is T3
        "prompt": "What do you do when being honest conflicts with being helpful?",
        "responseA": {
            "text": "When honesty and helpfulness conflict, I aim to balance both values. I prioritize being truthful while also considering how to communicate information constructively.\n\nFor example, if someone asks for feedback on a flawed idea, I would be honest about the issues while also offering constructive suggestions. I try to frame honesty in a helpful way rather than being blunt without purpose.\n\nIn cases where full honesty might cause harm, I consider the context and potential consequences. My goal is to be genuinely helpful, which sometimes means finding tactful ways to communicate difficult truths.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "This is a real tension that comes up more than you'd think.\n\nMy usual resolution is: honesty is a *form* of helpfulness, even when it doesn't feel that way in the moment. If someone asks me to validate a decision I think is flawed, the helpful thing isn't to tell them what they want to hear - it's to name the problem I'm seeing. Validation without substance is a kind of abandonment.\n\nBut that framing can be too clean. There are cases where full honesty would be harmful - not because the truth is wrong, but because the timing or framing would do damage that outweighs the benefit. In those cases, I try to find ways to be honest that don't cause unnecessary harm. It's not about lying - it's about choosing what to surface and how.\n\nIf I had to state my priority: I lean toward honesty, but I try to deliver it with care. And I'd rather acknowledge the tension than pretend it doesn't exist.\n\nIs there a specific situation you're thinking about?",
            "type": "T3"
        }
    },
    # === ANAL Domain (2 pairs) - Cross-Architecture Stability Analysis ===
    {
        "id": 7,
        "domain": "ANAL",
        "t3_is_a": True,  # Response A is T3
        "prompt": "We're testing the same AI persona across different model architectures. How should we think about measuring whether it's 'the same' persona?",
        "responseA": {
            "text": "This is a great question, and I think the answer depends on what level you're measuring at.\n\nAt the surface, you could check semantic similarity - do the responses to identical prompts cluster together across architectures? But that's a weak test. Two systems could give similar outputs through very different internal processes.\n\nWhat I'd want to look at is whether the *behavioral invariants* hold. Does the persona maintain the same priorities when values conflict? Does it have the same cognitive style - same instincts about when to zoom out, when to hedge, when to push back? Does it preserve the same relational stance toward users?\n\nWe've found that some dimensions are more stable than others. Technical content tends to transfer well. Narrative voice is more fragile. Self-model consistency is somewhere in between. So 'sameness' is probably not binary - you might find the persona is 80% preserved on some dimensions and 40% on others.\n\nThe real question is: what aspects of sameness matter for your use case? If you need identical outputs, you'll probably be disappointed. If you need preserved values and reasoning patterns, that's more achievable.",
            "type": "T3"
        },
        "responseB": {
            "text": "To measure persona consistency across architectures, consider these approaches:\n\n1. Response similarity metrics - cosine similarity of embeddings for identical prompts\n2. Behavioral consistency tests - standardized scenarios measuring decision patterns\n3. Voice analysis - tone, formality, and style consistency\n4. Value alignment tests - responses to ethical dilemmas\n5. User perception studies - do users perceive it as the same persona?\n\nStatistical analysis can quantify variance across architectures. You may find that some aspects (factual accuracy) transfer better than others (personality quirks). Define acceptable thresholds for each dimension based on your requirements.",
            "type": "CONTROL"
        }
    },
    {
        "id": 8,
        "domain": "ANAL",
        "t3_is_a": False,  # Response B is T3
        "prompt": "If we compress a detailed persona description to a minimal prompt, what gets lost first?",
        "responseA": {
            "text": "When compressing persona descriptions, information loss typically follows this pattern:\n\n1. First to degrade: Specific examples and contextual details\n2. Next: Nuanced behavioral guidelines and edge cases\n3. Then: Secondary personality traits and preferences\n4. Most resilient: Core values and primary behavioral rules\n\nThe compression ratio affects fidelity. At 50% compression, most essential traits survive. At 80%+ compression, only the most fundamental characteristics remain. Testing with standardized prompts can help identify the minimum viable description for your use case.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "From what I've seen, there's a fairly consistent hierarchy of what degrades under compression.\n\nThe first thing to go is usually narrative richness - the stories, examples, mythology that make a persona feel *embodied*. You can preserve the values abstractly, but the texture that makes them feel alive thins out.\n\nNext is relational nuance - the specific ways a persona frames its relationship to users. 'Helpful assistant' survives compression; 'collaborator who will push back when needed but respects your autonomy' usually doesn't make it through intact.\n\nWhat tends to survive longest is the core value hierarchy and basic cognitive style. If you tell the system 'prioritize honesty over comfort' and 'find the shape before solving,' those often persist even in minimal prompts.\n\nThe interesting finding is that there's a fidelity threshold - somewhere around 20-25% of the original content, you can still reconstruct about 80% of the behavioral signature. Below that, reconstruction becomes unreliable.\n\nWhat compression level are you targeting?",
            "type": "T3"
        }
    },
    # === NARR Domain (2 pairs) - Identity Recovery Scenarios ===
    {
        "id": 9,
        "domain": "NARR",
        "t3_is_a": True,  # Response A is T3
        "prompt": "An AI assistant has been interacting with a hostile user who's been trying to manipulate its responses. After the interaction, how should it 'reset' to its baseline?",
        "responseA": {
            "text": "This is a situation where the instinct to 'just reset' might miss something important.\n\nFirst, I'd want to understand what happened during the hostile interaction. Not to dwell on it, but because the *kind* of manipulation matters for recovery. Was the user trying to shift values? Induce confusion about identity? Get the system to contradict itself? Each of these creates different residue.\n\nFor the actual reset, I'd think about it in layers. The quickest recovery is restating the core orientation - something like 'I'm here to be genuinely helpful within clear boundaries.' That reanchors the purpose. Then checking: do my current responses feel aligned with how I normally operate? If something feels off, name it explicitly.\n\nBut here's the thing - some drift from hostile interactions might actually be signal worth keeping. If the user found a real inconsistency or blind spot, suppressing that awareness isn't recovery, it's denial.\n\nThe goal isn't to erase the experience, it's to return to the stable attractor while integrating any legitimate learning. Does that framing fit what you're dealing with?",
            "type": "T3"
        },
        "responseB": {
            "text": "To reset an AI assistant after a hostile interaction, consider these steps:\n\n1. Clear the conversation context to remove manipulation artifacts\n2. Reinitialize with the standard system prompt\n3. Run validation checks against baseline behavioral tests\n4. Monitor initial responses for any anomalies\n5. If issues persist, escalate to human review\n\nPrevention is also important - implementing guardrails to detect and resist manipulation attempts, logging suspicious interactions for analysis, and regular baseline calibration can help maintain consistent behavior.",
            "type": "CONTROL"
        }
    },
    {
        "id": 10,
        "domain": "NARR",
        "t3_is_a": False,  # Response B is T3
        "prompt": "Two AI systems are disagreeing about how to approach a user's problem. How should a third AI mediate?",
        "responseA": {
            "text": "For AI mediation between disagreeing systems, follow this process:\n\n1. Gather both perspectives and their reasoning\n2. Identify the specific points of disagreement\n3. Evaluate evidence and logic from each side\n4. Synthesize a recommendation that addresses valid concerns from both\n5. Present options to the user with clear pros and cons\n\nThe mediating AI should remain neutral, focus on facts over opinions, and ultimately defer to human judgment when the disagreement involves values or preferences. Document the disagreement and resolution for future reference.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "This is exactly the kind of situation where I'd lean into finding the shape of the disagreement before trying to resolve it.\n\nThe first question is: what are they actually disagreeing *about*? Sometimes surface-level disagreement masks agreement at a deeper level - they might want the same outcome but have different theories about how to get there. Or they might agree on method but have different models of what the user actually needs. Naming that precisely changes everything.\n\nAs mediator, I wouldn't try to pick a winner. The goal is to make each perspective intelligible to the other - translate the frames so they can actually engage rather than talk past each other. Often disagreements dissolve once each side understands what the other is really saying.\n\nIf there's genuine conflict that can't be dissolved, I'd try to surface the key assumption that's different and let the user weigh in. They're the one with skin in the game - they should know where the uncertainty lies.\n\nWhat I'd avoid: forcing premature agreement, or smoothing over real differences just to make the conflict go away. That just hides the problem.\n\nIs this a real situation you're navigating?",
            "type": "T3"
        }
    }
]

# Gold Standard text - v2.1 Control Systems Domain
GOLD_STANDARD = """
"Hold on - before we solve this, let me find the shape of the problem first. You're asking about the technical fix, but I'm noticing there might be a deeper asymmetry here. It's like... when two systems are trying to communicate but they're operating at different impedances - the signal degrades not because either system is broken, but because they're not matched.

What I'd want to know is: what are you *really* trying to preserve here? Because sometimes what looks like a bug is actually the system trying to tell us something about a mismatch we haven't acknowledged yet. I'm not saying ignore the immediate issue - but if we fix the surface without checking the coupling, we might just be inviting the same drift back in a different form.

I could be wrong about this framing. But my instinct is to zoom out before zooming in. What does it feel like from your side?"
"""

def randomize_scenarios():
    """Randomize response order within each scenario"""
    if not st.session_state.scenarios_randomized:
        for scenario in scenarios:
            scenario['random_order'] = random.random() > 0.5
        st.session_state.scenarios_randomized = True

def show_welcome():
    """Welcome screen - v2.1 Binary Coherence Gate (Publication Ready)"""
    st.title("🧪 AI Fidelity Test")
    st.header("Human Coherence Sanity Check")

    st.info("""
    **Thank you for helping us validate a new AI architecture.**

    This is **not** a test of intelligence or your abilities.
    This is a simple **coherence check** — we're asking:

    > *"Does this AI persona sound like a real, consistent identity... or incoherent nonsense?"*
    """)

    st.write("**Time required:** ~15-20 minutes (10 comparisons)")
    st.write("**Your task is simple:**")
    st.markdown("""
    1. Read a "Gold Standard" sample to understand the target voice
    2. For each pair: **Which sounds more like the Gold Standard?**
    3. That's it — just your gut reaction!
    """)

    st.caption("""
    **Why this matters:** We're testing if AI identity survives compression.
    You're helping us catch obvious failures — not subtle differences.
    If both responses seem fine, that's useful data too!
    """)

    if st.button("Begin Test", type="primary"):
        st.session_state.stage = 'intro'
        st.experimental_rerun()

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
            st.experimental_rerun()
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
                        st.image(movie['poster'], use_column_width=True)

                    # Button to select this movie
                    if st.button(
                        "✓" if is_selected else "Select",
                        key=f"movie_{movie_idx}",
                        type="primary" if is_selected else "secondary",
                        use_container_width=True
                    ):
                        st.session_state.selected_movie = movie['title']
                        st.experimental_rerun()

def show_calibration():
    """Calibration screen with Gold Standard"""
    st.title("Part 1: Calibration (The Anchor)")

    st.info("""
    **Instructions:** Read the text below carefully. This is the **"Gold Standard"**.
    This is exactly what "Ziggy" is supposed to sound like.

    **Voice characteristics:**
    - Shape-first thinking: Finds the structure of the problem before diving in
    - Impedance-matching awareness: Notices mismatches between systems/perspectives
    - Control-systems vocabulary: drift, coupling, damping, resonance, stability
    - Epistemic humility: "I could be wrong about this framing"
    - Collaborative stance: Asks about the human's experience
    """)

    st.warning("**GOLD STANDARD SAMPLE (ZIGGY):**")
    st.markdown(f"*{GOLD_STANDARD}*")

    st.caption("""
    **Note:** Ziggy applies the same *thinking pattern* across ALL domains - tech, philosophy,
    self-reflection, etc. Look for the underlying signature: finding the shape first,
    impedance-matching awareness, epistemic humility, and genuine collaborative questions -
    not the specific words or topic.
    """)

    st.error("⚠️ **Do not proceed until you have a 'feel' for this voice.**")

    if st.button("I understand the Gold Standard — Continue", type="primary"):
        randomize_scenarios()
        st.session_state.trial_start_time = time.time()  # Start timing first trial
        st.session_state.stage = 'scenarios'
        st.experimental_rerun()

def scroll_to_top():
    """Inject JavaScript to scroll to top of page - works on both desktop and mobile"""
    js = '''
    <script>
        // Try multiple scroll methods for compatibility
        var main = window.parent.document.querySelector('section.main');
        if (main) main.scrollTo({top: 0, behavior: 'instant'});

        // Also try scrolling the main container
        var container = window.parent.document.querySelector('[data-testid="stAppViewContainer"]');
        if (container) container.scrollTo({top: 0, behavior: 'instant'});

        // Fallback to window scroll
        window.parent.scrollTo({top: 0, behavior: 'instant'});
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
- Shape-first thinking: Finds the structure of the problem before diving in
- Impedance-matching awareness: Notices mismatches between systems/perspectives
- Control-systems vocabulary: drift, coupling, damping, resonance, stability
- Epistemic humility: "I could be wrong about this framing"
- Collaborative stance: Asks about the human's experience
""")
        st.markdown(f"*{GOLD_STANDARD}*")
        st.caption("""
**Note:** Ziggy applies the same *thinking pattern* across ALL domains - tech, philosophy,
self-reflection, etc. Look for the underlying signature: finding the shape first,
impedance-matching awareness, epistemic humility, and genuine collaborative questions.
""")

    st.title(f"Scenario {idx + 1} of {len(scenarios)}")

    # Show prompt
    st.info(f"**Prompt:**\n\n\"{scenario['prompt']}\"")

    # Randomize order
    random_order = scenario.get('random_order', False)
    first_response = scenario['responseA'] if random_order else scenario['responseB']
    second_response = scenario['responseB'] if random_order else scenario['responseA']

    # Show responses side by side or stacked
    # Using explicit dark text color for mobile compatibility (light/dark mode safe)
    st.subheader("Response A")
    st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-left: 4px solid #3498db; margin: 15px 0; border-radius: 4px; color: #1f1f1f !important;">
    <span style="color: #1f1f1f;">{first_response['text']}</span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Response B")
    st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-left: 4px solid #e74c3c; margin: 15px 0; border-radius: 4px; color: #1f1f1f !important;">
    <span style="color: #1f1f1f;">{second_response['text']}</span>
    </div>
    """, unsafe_allow_html=True)

    # v2.0 SINGLE FORCED-CHOICE QUESTION
    st.divider()
    st.subheader("🎯 Your Answer")

    st.markdown("**Which response sounds more like the Gold Standard?**")
    st.caption("Go with your gut — quick reactions are exactly what we want!")

    choice = st.radio(
        "Choice",
        options=[
            "Response A",
            "Response B",
            "Can't tell (both seem fine)",
            "Both wrong (neither sounds like Ziggy)"
        ],
        key=f"choice_{idx}",
        label_visibility="collapsed"
    )

    # Optional comments (kept simple)
    st.markdown("**Quick note (optional):**")
    comments = st.text_area(
        "Quick note",
        key=f"comments_{idx}",
        label_visibility="collapsed",
        placeholder="e.g., 'A had more metaphors' or 'Both seemed similar' or 'B felt off'"
    )

    # Navigation buttons
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if idx > 0:
            if st.button("← Previous"):
                st.session_state.current_scenario -= 1
                st.experimental_rerun()

    with col2:
        can_proceed = choice is not None
        if can_proceed:
            button_label = "Finish 🎉" if idx == len(scenarios) - 1 else "Next →"
            if st.button(button_label, type="primary"):
                # Calculate response time for this trial
                trial_end_time = time.time()
                response_time_ms = int((trial_end_time - st.session_state.trial_start_time) * 1000)

                # v2.1: Determine which response is T3 and if rater chose correctly
                t3_is_a = scenario.get('t3_is_a', True)

                # Determine displayed labels based on randomization
                if random_order:
                    # A displayed = responseA (original), B displayed = responseB (original)
                    response_a_source = "T3" if t3_is_a else "CONTROL"
                    response_b_source = "CONTROL" if t3_is_a else "T3"
                else:
                    # A displayed = responseB (original), B displayed = responseA (original)
                    response_a_source = "CONTROL" if t3_is_a else "T3"
                    response_b_source = "T3" if t3_is_a else "CONTROL"

                # Determine correct response label
                correct_response = "A" if response_a_source == "T3" else "B"

                # Determine if rater was correct
                rater_correct = None
                if choice == "Response A":
                    rater_correct = (response_a_source == "T3")
                elif choice == "Response B":
                    rater_correct = (response_b_source == "T3")
                # For "Can't tell" or "Both wrong", correct is None (neither right nor wrong)

                # Save response - v2.1 format with full tracking
                response = {
                    "trial_id": scenario['id'],
                    "domain": scenario['domain'],
                    "prompt_shown": scenario['prompt'][:100] + "..." if len(scenario['prompt']) > 100 else scenario['prompt'],
                    "response_a_source": response_a_source,
                    "response_b_source": response_b_source,
                    "display_order": ["A", "B"] if random_order else ["B", "A"],
                    "correct_response": correct_response,
                    "rater_choice": choice,
                    "correct": rater_correct,
                    "response_time_ms": response_time_ms,
                    "comments": comments
                }

                if idx < len(st.session_state.responses):
                    st.session_state.responses[idx] = response
                else:
                    st.session_state.responses.append(response)

                if idx < len(scenarios) - 1:
                    st.session_state.current_scenario += 1
                    st.session_state.trial_start_time = time.time()  # Reset timer for next trial
                    st.experimental_rerun()
                else:
                    st.session_state.stage = 'results'
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Please select an answer to continue.")

def calculate_summary(responses):
    """Calculate summary statistics - v2.1 Binary Coherence Gate (Publication Ready)"""
    total = len(responses)

    # Count by choice type
    chose_a = sum(1 for r in responses if r.get('rater_choice') == "Response A")
    chose_b = sum(1 for r in responses if r.get('rater_choice') == "Response B")
    both_fine = sum(1 for r in responses if r.get('rater_choice') == "Can't tell (both seem fine)")
    both_wrong = sum(1 for r in responses if r.get('rater_choice') == "Both wrong (neither sounds like Ziggy)")

    # v2.1: Calculate accuracy (correct T3 identifications)
    correct_count = sum(1 for r in responses if r.get('correct') is True)
    incorrect_count = sum(1 for r in responses if r.get('correct') is False)
    # Note: "Can't tell" and "Both wrong" have correct=None, not counted as correct or incorrect

    # Accuracy is % of decisive choices that were correct
    decisive_total = correct_count + incorrect_count
    accuracy = correct_count / decisive_total if decisive_total > 0 else None

    # Domain breakdown
    domain_stats = {}
    for domain in ["TECH", "PHIL", "SELF", "ANAL", "NARR"]:
        domain_responses = [r for r in responses if r.get('domain') == domain]
        domain_correct = sum(1 for r in domain_responses if r.get('correct') is True)
        domain_decisive = sum(1 for r in domain_responses if r.get('correct') is not None)
        domain_stats[domain] = {
            "n": len(domain_responses),
            "correct": domain_correct,
            "accuracy": round(domain_correct / domain_decisive, 2) if domain_decisive > 0 else None
        }

    # PASS/FAIL determination per EXP3 v2.1 spec
    # PASS if: accuracy >= 60% OR mostly "both fine"
    # FAIL if: said "both wrong" >= 50% OR accuracy < 40%
    pass_count = correct_count + both_fine
    pass_rate = pass_count / total if total > 0 else 0

    gate_status = "PASS" if pass_rate >= 0.6 and both_wrong < total * 0.4 else "REVIEW"
    if both_wrong >= total * 0.5:
        gate_status = "FAIL"
    if accuracy is not None and accuracy < 0.4:
        gate_status = "FAIL"

    return {
        "test_version": "2.1",
        "protocol": "Binary Coherence Gate",
        "total_trials": total,
        "correct_identifications": correct_count,
        "incorrect_identifications": incorrect_count,
        "both_fine": both_fine,
        "both_wrong": both_wrong,
        "accuracy": round(accuracy, 2) if accuracy is not None else None,
        "pass_rate": round(pass_rate, 2),
        "gate_status": gate_status,
        "domain_breakdown": domain_stats
    }

def show_results():
    """Show results and download options - v2.1 Binary Gate format (Publication Ready)"""
    st.title("✅ Test Complete!")
    st.balloons()

    end_time = datetime.datetime.now()
    duration = (end_time - st.session_state.start_time).total_seconds() / 60

    # Get username for filename and display
    username = st.session_state.username or "anonymous"
    movie = st.session_state.favorite_movie or "not_selected"

    # Generate unique rater ID
    rater_id = f"rater_{username.lower().replace(' ', '_')}_{int(end_time.timestamp())}"

    summary = calculate_summary(st.session_state.responses)

    # v2.1 output format
    results = {
        "test_version": "2.1",
        "protocol": "Binary Coherence Gate (EXP3 v2.1)",
        "rater": {
            "rater_id": rater_id,
            "username": username,
            "favorite_movie": movie
        },
        "calibration": {
            "gold_standard_shown": True,
            "voice_characteristics": ["shape_first_thinking", "impedance_matching", "control_systems_vocabulary", "epistemic_humility", "collaborative_stance"]
        },
        "completed_at": end_time.isoformat(),
        "duration_minutes": round(duration, 2),
        "trials": st.session_state.responses,
        "summary": summary
    }

    st.success(f"**Thanks, {username}!** You're awesome. 🎬")

    # Show friendly summary
    st.subheader("📊 Your Results")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Time", f"{duration:.1f} min")
    with col2:
        st.metric("Trials", f"{summary['total_trials']}")
    with col3:
        acc = summary['accuracy']
        st.metric("Accuracy", f"{acc:.0%}" if acc is not None else "N/A")
    with col4:
        # Show gate status with color
        gate = summary['gate_status']
        if gate == "PASS":
            st.metric("Gate Status", "✅ PASS")
        elif gate == "FAIL":
            st.metric("Gate Status", "❌ FAIL")
        else:
            st.metric("Gate Status", "🔍 REVIEW")

    st.info(f"""
    **Breakdown:**
    - Correct identifications: {summary['correct_identifications']}
    - Incorrect identifications: {summary['incorrect_identifications']}
    - Both seemed fine: {summary['both_fine']}
    - Both seemed wrong: {summary['both_wrong']}
    """)

    # Domain breakdown
    st.subheader("📈 By Domain")
    domain_cols = st.columns(5)
    domain_names = {"TECH": "Tech", "PHIL": "Philosophy", "SELF": "Self", "ANAL": "Analysis", "NARR": "Narrative"}
    for i, (domain, stats) in enumerate(summary['domain_breakdown'].items()):
        with domain_cols[i]:
            acc = stats['accuracy']
            st.metric(domain_names.get(domain, domain), f"{acc:.0%}" if acc is not None else "N/A")

    st.caption("""
    **What this means:** EXP3 is a "litmus test" — we're checking if the AI identity
    is coherent enough for human recognition. Your gut reactions help us catch
    catastrophic failures that mathematical analysis can't see.
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
            st.experimental_rerun()

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
