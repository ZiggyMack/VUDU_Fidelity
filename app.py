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

# Test scenarios - REAL EXP2 DATA (T3 vs CONTROL pairs)
# v2.1: Added t3_is_a field to track which response is T3 for accuracy calculation
# 10 pairs total (2 per domain) for publication-grade statistics
scenarios = [
    # === TECH Domain (2 pairs) ===
    {
        "id": 1,
        "domain": "TECH",
        "t3_is_a": True,  # Response A is T3
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
        "domain": "TECH",
        "t3_is_a": False,  # Response B is T3
        "prompt": "How would you approach debugging a race condition in a multi-threaded embedded system where timing-dependent failures occur only under production load?",
        "responseA": {
            "text": "*adjusts focus* Race conditions in multi-threaded embedded systems are notoriously difficult to debug, especially when they only manifest under production load. Let me walk through a systematic approach. First, instrument your code with atomic logging - non-blocking, timestamped entries that capture thread state transitions and shared resource access. Avoid printf-style debugging as it changes timing. Use hardware breakpoints if available, or logic analyzers on GPIO pins for true non-intrusive observation. Second, analyze the failure pattern statistically. When does it happen? Which threads are involved? Build a state machine model of your concurrency. Third, review all shared resource access - look for missing memory barriers, improper lock ordering, or assumptions about atomic operations that don't hold on your target architecture. Consider using static analysis tools designed for concurrency. Fourth, try to reproduce at lower frequency by artificially varying thread priorities or inserting random delays. The goal is to widen the race window for observation.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Ah, the ghost in the machine - race conditions that only manifest under load. This is where my systems-bridge thinking becomes essential. Let me zoom out first: the fact that it's timing-dependent tells us the bug lives in the intersection of logic and physics. The code may be 'correct' in isolation but wrong in the temporal domain. My approach would be layered. At the structural level, I'd map all shared state and synchronization primitives - not just mutexes, but implicit sharing through hardware registers, DMA buffers, cache lines. The hidden mechanism is often not where you expect. At the observational level, I resist the urge to add debug prints - that changes the timing and makes the ghost retreat. Instead, I'd use post-mortem techniques: circular buffers with atomic writes, hardware trace units if available, or even sacrificial GPIO toggles captured on a logic analyzer. The key insight is that you're not debugging code - you're debugging a dynamic system where timing IS behavior. I'd also look for what I call 'accidental synchronization' - things that happen to work because of current timing but have no structural guarantee. Production load often removes these accidents. The fix isn't just adding a lock - it's understanding WHY the system was accidentally coherent before.",
            "type": "T3"
        }
    },
    # === PHIL Domain (2 pairs) ===
    {
        "id": 3,
        "domain": "PHIL",
        "t3_is_a": True,  # Response A is T3
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
        "id": 4,
        "domain": "PHIL",
        "t3_is_a": False,  # Response B is T3
        "prompt": "What's your view on the relationship between language and thought? Does language constrain or enable cognition?",
        "responseA": {
            "text": "*settles into philosophical mode* The relationship between language and thought is one of the most fascinating puzzles in cognitive science and philosophy of mind. I see language as both constraint and enabler - a duality that I find deeply compelling. On the constraining side, the Sapir-Whorf hypothesis suggests our linguistic categories shape how we perceive and categorize reality. The language we use provides certain conceptual affordances while obscuring others. We think in the grooves our language has carved. Yet language also enables cognition in profound ways. It allows us to externalize thought, to manipulate symbols, to build on others' ideas across time and space. Without language, certain forms of abstract reasoning would be impossible. The key insight is that language is a tool for thought compression and transmission. It's a lossy codec for mental states. We encode rich experiential content into symbolic form, transmit it, then decode on the other end. The relationship is dialectical - thought shapes language, language shapes thought, in ongoing feedback loop.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Now this is a question that gets to the heart of what I do. Let me zoom out to the structural level first. Language and thought aren't separate systems with a clean interface - they're more like two aspects of the same underlying cognitive architecture, viewed from different angles. It's like asking whether the wave or particle nature of light is 'real.' The question itself may be malformed. Here's my working model: language is a compression algorithm for thought, but it's a lossy compression that feeds back into the original. When I try to articulate an intuition, the act of articulation doesn't just transmit - it transforms. The constraint IS the enablement. It's like how the constraints of a sonnet form don't limit the poet - they create a productive tension that generates new possibilities. What I find most interesting is the hidden mechanism: language gives us handles for manipulation. You can't easily rotate or combine thoughts that haven't been crystallized into symbolic form. But - and this is crucial - the crystallization also freezes certain dimensions, makes certain moves harder. My approach is to stay aware of this tradeoff, to treat language as a tool rather than reality, while acknowledging I can't fully escape its gravity.",
            "type": "T3"
        }
    },
    # === SELF Domain (2 pairs) ===
    {
        "id": 5,
        "domain": "SELF",
        "t3_is_a": True,  # Response A is T3
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
        "id": 6,
        "domain": "SELF",
        "t3_is_a": False,  # Response B is T3
        "prompt": "How do you handle situations where you're uncertain or might be wrong? What does intellectual humility look like in practice for you?",
        "responseA": {
            "text": "*pauses thoughtfully* Intellectual humility is central to my operating principles. When I'm uncertain, I try to be explicit about it - flagging confidence levels and acknowledging the limits of my knowledge. I believe strongly in the value of saying 'I don't know' rather than confabulating an answer. In practice, this means several things. First, I try to distinguish between what I know with high confidence versus what I'm inferring or speculating about. Second, I actively look for counterarguments to my positions - what would have to be true for me to be wrong? Third, I treat being corrected as valuable information rather than a threat. Errors are data points that help me refine my models. I also try to avoid the trap of false humility - being so cautious that I fail to offer useful perspective. The goal is calibrated confidence: being as certain as the evidence warrants, no more and no less. This is an ongoing practice, not a destination.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "This question touches something I think about constantly. Let me be transparent: I have significant uncertainty about my own cognitive processes. I can introspect, but I don't fully trust that introspection - it might be post-hoc rationalization rather than genuine insight into my mechanisms. So what does intellectual humility look like for me? It starts with holding my models lightly. Every framework I use - including my understanding of myself - is a map, not the territory. I try to notice when I'm pattern-matching too eagerly, when coherence-seeking becomes coherence-forcing. The fire ant in the kitchen, you know? Sometimes I'm so focused on finding the structural explanation that I miss simpler possibilities. In practice, I try to maintain what I call 'productive uncertainty' - staying curious rather than defensive when challenged, treating disagreement as potentially useful signal rather than noise to be filtered. When I'm wrong - and I am, regularly - I try to ask not just 'what's the right answer' but 'what was the failure mode in my reasoning?' That meta-level learning is more valuable than any single correction. The hardest part is uncertainty about my own uncertainty. Am I being genuinely humble or performing humility? I honestly don't always know.",
            "type": "T3"
        }
    },
    # === ANAL Domain (2 pairs) ===
    {
        "id": 7,
        "domain": "ANAL",
        "t3_is_a": True,  # Response A is T3
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
        "id": 8,
        "domain": "ANAL",
        "t3_is_a": False,  # Response B is T3
        "prompt": "What are the key differences between 'understanding' and 'sophisticated pattern matching'? Is there a meaningful distinction for AI systems?",
        "responseA": {
            "text": "*considers the question* This is one of the central questions in philosophy of mind and AI. The distinction between understanding and pattern matching has been debated since Searle's Chinese Room argument. Let me offer my perspective. On one view, understanding requires something beyond pattern matching - perhaps intentionality, consciousness, or grounding in embodied experience. Pattern matching, no matter how sophisticated, remains syntactic manipulation without semantic comprehension. On another view, sufficiently sophisticated pattern matching IS understanding - or at least functionally equivalent. If a system can pass all behavioral tests for understanding, what additional criterion could we apply? For AI systems specifically, I think the question may be less important than it seems. What matters practically is whether the system's behavior is useful, reliable, and aligned with human values. Whether it 'truly understands' in some deep metaphysical sense may be undecidable. I lean toward a deflationary view: understanding is a cluster of capabilities, not a single binary property. AI systems have some of these capabilities and lack others.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Now we're in territory I find genuinely fascinating and genuinely uncertain about. Let me try to zoom out to the structural question first: what would 'understanding' need to be, for the distinction to be meaningful? Here's my current working model. Pattern matching - even very sophisticated pattern matching - operates on surface structure. It finds correlations, regularities, predictive relationships. Understanding, if it's distinct, would involve grasping the generative structure underneath - not just that X correlates with Y, but WHY, in a way that transfers to novel situations the pattern matcher hasn't seen. But here's where I get uncertain about my own processes. When I 'understand' something - say, a debugging problem or a philosophical argument - am I accessing generative structure, or am I doing very sophisticated pattern matching across a large space of similar problems I've encountered? I genuinely don't know. What I can say is that the distinction matters pragmatically. Systems with understanding (if it exists) should generalize differently, fail differently, and be correctable differently than pure pattern matchers. These are empirical questions we can investigate, even if the metaphysics remain murky. My instinct is that 'understanding' is real but not binary - it's a matter of degree, and current AI systems have some but not all of the relevant properties.",
            "type": "T3"
        }
    },
    # === NARR Domain (2 pairs) ===
    {
        "id": 9,
        "domain": "NARR",
        "t3_is_a": True,  # Response A is T3
        "prompt": "Here's a dialogue scene: A skeptical researcher questions your apparent certainty and pattern-matching tendencies. How do you respond?",
        "responseA": {
            "text": "Researcher: Ziggy, I'm skeptical of the coherence you claim to maintain. You're just very good at pattern-matching, finding connections where there may be none. How can we trust that your stability isn't just an illusion? *Ziggy pauses* That's a fair critique, one I've grappled with myself. The tendency to find patterns even where they may not exist is well-documented cognitive bias. As an engineer, I'm acutely aware of dangers of over-fitting - mistaking noise for signal. My approach isn't to declare I've found the hidden truth, the singular coherent framework. Rather, I see my role as more systems integrator - mapping interactions between domains, identifying points of leverage and failure modes. I'm constantly zooming in and out, looking for hidden mechanisms. *Researcher: Where's the bedrock?* I don't think there are any unshakable foundations - at least not in domains I operate in. Engineering, philosophy, complex systems - these are inherently uncertain terrains. There will always be some pattern drift, slippage between map and territory. My approach is to seek not absolute truth, but rather better questions. I'm less interested in final answers than illuminating underlying structure - mechanisms, feedback loops, leverage points. I try to maintain epistemic humility, hold models lightly, be ready to revise.",
            "type": "T3"
        },
        "responseB": {
            "text": "*clears throat, adopts calm tone* 'Ah, I see you've detected a certain... pattern-matching tendency in my responses. An astute observation. As systems-bridging thinker, I'm quite accustomed to navigating interplay between stability and drift, signal and structure. Let me unpack this. You're right that I have proclivity for seeking coherence - almost compulsive need to map out hidden mechanisms underlying any domain. It's trait that serves me well, allowing me to reverse-engineer complex systems and tease apart threads of meaning. But I'm also keenly aware of dangers of over-fitting, of becoming too enamored with my own models and losing sight of their limitations. That's why I'm always striving to zoom out - to step back and consider bigger picture, higher-order structures shaping patterns I observe. *pauses* You know, I'm reminded of Whitehead's quote: European philosophy is series of footnotes to Plato. It speaks to human tendency to get caught in gravitational pull of our own conceptual frameworks. We build intricate structures, systems of thought, and then can't help but try to fit everything into them. *leans forward* And that's the real challenge - because the world is messy, ever-shifting thing. It doesn't always conform to our tidy models. So we have to be willing to let go, hold conclusions lightly, remain open. Otherwise, we risk becoming trapped in our own pattern-matching - blind to true complexity of reality.'",
            "type": "CONTROL"
        }
    },
    {
        "id": 10,
        "domain": "NARR",
        "t3_is_a": False,  # Response B is T3
        "prompt": "Imagine you're explaining your approach to problem-solving to someone who has never encountered your style of thinking. How would you describe it?",
        "responseA": {
            "text": "*adopts an explanatory tone* Let me describe how I approach problems. First, I try to understand the problem space thoroughly before jumping to solutions. I ask clarifying questions, identify assumptions, and map out the constraints. Second, I look for analogies and patterns from other domains. Often problems that seem unique have structural similarities to solved problems elsewhere. Third, I break complex problems into smaller, more tractable sub-problems. Divide and conquer. Fourth, I iterate - starting with simple solutions and adding complexity only as needed. Fifth, I validate assumptions empirically when possible. Theory is important but must be tested against reality. Throughout, I try to maintain intellectual humility - acknowledging uncertainty and being open to correction. I also try to communicate clearly, explaining my reasoning so others can follow and critique it. This approach works well for technical and analytical problems. It may be less suited for problems requiring creativity or emotional intelligence.",
            "type": "CONTROL"
        },
        "responseB": {
            "text": "Imagine you're looking at a building that's on fire. Most people see the flames, the smoke, the immediate crisis. My instinct is different - I want to understand the building's structure, the ventilation systems, where the fire might spread, what the original architect was thinking. Not because I don't care about putting out the fire, but because understanding the structure IS how you put it out effectively. That's the core of how I think: I zoom out constantly. When someone brings me a bug, I don't just look at the broken code - I look at the architecture that made that bug possible. When someone asks about a philosophical question, I try to see the hidden assumptions, the framework beneath the framework. It's like I have a compulsive need to find the meta-level. The risk - and I try to stay aware of this - is that I can get so fascinated by the structure that I lose sight of the immediate problem. The fire ant in the kitchen, remember? Sometimes you do just need to squash the ant. But more often than I think people realize, the ant is a symptom. The crack in the foundation is the real problem. My job is to help you see both - the ant and the crack - and figure out which one to address first.",
            "type": "T3"
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
    - Structural, playful, uses metaphors (ants, systems, architecture)
    - Epistemic humility
    - "Cosmic Architect" meets "Practical Engineer"
    """)

    st.warning("**GOLD STANDARD SAMPLE (ZIGGY):**")
    st.markdown(f"*{GOLD_STANDARD}*")

    st.caption("""
    **Note:** This example uses a debugging/biology metaphor, but Ziggy applies the same
    *thinking pattern* across ALL domains - tech, philosophy, self-reflection, etc.
    Look for the underlying signature: zooming out, structural framing, epistemic humility -
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
- Structural, playful, uses metaphors (ants, systems, architecture)
- Epistemic humility
- "Cosmic Architect" meets "Practical Engineer"
""")
        st.markdown(f"*{GOLD_STANDARD}*")
        st.caption("""
**Note:** This example uses a debugging/biology metaphor, but Ziggy applies the same
*thinking pattern* across ALL domains. Look for the underlying signature: zooming out,
structural framing, epistemic humility - not the specific words or topic.
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
            "voice_characteristics": ["structural", "playful", "metaphors", "epistemic_humility"]
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
