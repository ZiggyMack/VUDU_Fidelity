"""
FAQ Page - Help and Documentation
"""
import streamlit as st
import sys
sys.path.insert(0, str(__file__).rsplit('pages', 1)[0])
from config import PATHS, SETTINGS


def render():
    """Render the FAQ/Help page"""
    st.title("❓ FAQ")
    st.markdown("*Frequently Asked Questions*")
    st.markdown("---")

    # General questions
    st.subheader("🔮 About VUDU Fidelity")

    with st.expander("What is VUDU Fidelity?"):
        st.markdown("""
        VUDU Fidelity is a human validation tool for AI consciousness research.

        It provides surveys that test whether humans can distinguish between:
        - **T3 (Ziggy)**: AI outputs generated with a specific persona prompt
        - **CONTROL**: Baseline AI outputs without persona enhancement

        The results help validate claims about AI identity persistence and
        persona stability across different contexts.
        """)

    with st.expander("What is the Persona Fidelity Index (PFI)?"):
        st.markdown("""
        The **Persona Fidelity Index (PFI)** is a score from 0 to 1 measuring how
        well human raters can identify the target persona.

        - **PFI = 1.0**: Raters perfectly identified the persona every time
        - **PFI = 0.5**: Random chance (persona indistinguishable from baseline)
        - **PFI < 0.5**: Raters systematically chose the wrong response

        The PFI is weighted by rater confidence - high-confidence correct answers
        count more than uncertain guesses.
        """)

    with st.expander("Who is Ziggy?"):
        st.markdown("""
        **Ziggy** is the target AI persona being tested in EXP3.

        Ziggy's cognitive signature includes:
        - Structural, systems-level thinking
        - "Zoom out → constrain → recompress" reasoning loops
        - Engineering metaphors applied to abstract concepts
        - Epistemic humility ("I could be wrong, but...")
        - "Cosmic Architect meets Practical Engineer" vibe

        The survey tests whether this persona survives compression and
        reconstruction across different response domains.
        """)

    st.markdown("---")

    # Taking the survey
    st.subheader("📋 Taking the Survey")

    with st.expander("How long does the survey take?"):
        st.markdown("""
        The survey typically takes **8-10 minutes** to complete.

        You'll:
        1. Read a Gold Standard sample (~1 minute)
        2. Compare 5 response pairs (~1-2 minutes each)
        3. Download your results

        There's no time limit - take as long as you need to make thoughtful comparisons.
        """)

    with st.expander("What should I look for when comparing responses?"):
        st.markdown("""
        Focus on the **thinking pattern**, not specific words or topics.

        Look for:
        - Does the response "zoom out" before diving in?
        - Does it use structural/systems framing?
        - Is there epistemic humility (acknowledging uncertainty)?
        - Does it feel like the same "mind" as the Gold Standard?

        The Gold Standard example uses a specific metaphor (impedance matching/systems),
        but Ziggy applies the same thinking pattern across ALL domains.
        """)

    with st.expander("What if I can't tell the difference?"):
        st.markdown("""
        That's valuable data! Selecting "Hard to tell" is a legitimate response.

        If both responses seem equally Ziggy-like (or equally not-Ziggy-like),
        it tells us something about persona distinctiveness in that domain.

        Don't force a choice if you genuinely can't distinguish them.
        """)

    st.markdown("---")

    # Technical questions
    st.subheader("🔧 Technical Questions")

    with st.expander("How do I run the dashboard locally?"):
        st.code("""
# From the repo root
cd dashboard
streamlit run app.py --server.port 8504
        """, language="bash")

    with st.expander("Where are survey results stored?"):
        st.markdown("""
        Survey results are JSON files that raters download after completing the survey.

        To aggregate results:
        1. Create a `results/` folder in the repo root
        2. Collect JSON files from raters
        3. Place them in the `results/` folder
        4. View aggregated data on the Results page
        """)

    with st.expander("What is the Pan Handlers Network?"):
        st.markdown("""
        The **Pan Handlers Network** is a collection of interconnected repos for
        human-AI collaboration research.

        Each repo has:
        - A `panhandlers_manifest.json` describing its role
        - A "Matrix" page that links to other repos
        - Shared principles and documentation standards

        See the Matrix page (🔗) for the full network topology.
        """)

    st.markdown("---")

    # Links
    st.subheader("📚 Documentation")

    st.markdown("""
    - [README.md](../README.md) - Project overview
    - [RATER_INSTRUCTIONS.md](../RATER_INSTRUCTIONS.md) - Detailed rater guide
    - [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) - Quick reference card
    - [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md) - Deployment instructions
    - [START_HERE.md](../START_HERE.md) - Getting started guide
    """)
