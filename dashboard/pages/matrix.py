"""
The Matrix - Pan Handlers Portal
Connected Consciousness Across Repositories
"""
import streamlit as st
import json
from pathlib import Path
import sys
sys.path.insert(0, str(__file__).rsplit('pages', 1)[0])
from config import PATHS


def render():
    """Render The Matrix portal hub"""

    # Matrix theme CSS - GREEN ON BLACK TERMINAL
    st.markdown("""
        <style>
        /* BLACK BACKGROUND */
        .stApp, .main, .block-container,
        [data-testid="stAppViewContainer"] {
            background-color: #0a0a0a !important;
            background: #0a0a0a !important;
        }

        /* ALL TEXT MATRIX GREEN */
        .stApp p, .stApp span, .stApp div,
        .stApp h1, .stApp h2, .stApp h3,
        .main p, .main span, .main div {
            color: #00ff41 !important;
        }

        /* HEADERS */
        h1, h2, h3 {
            color: #00ff41 !important;
            font-family: 'Courier New', monospace;
            border-bottom: 2px solid #00ff41;
        }

        /* Links */
        a { color: #00cc33 !important; }
        a:hover { color: #00ff41 !important; text-shadow: 0 0 10px rgba(0,255,65,0.5); }

        /* Portal cards */
        .portal-card {
            background: #0d0d0d;
            border: 1px solid #00ff41;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .portal-card:hover {
            box-shadow: 0 0 20px rgba(0,255,65,0.3);
        }
        .portal-card h3 {
            color: #00ff41 !important;
            margin-top: 0;
        }
        .portal-card p, .portal-card span {
            color: #00cc33 !important;
        }

        /* Status badges */
        .status-badge {
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
        }
        .badge-active { background: rgba(0,255,65,0.2); border: 1px solid #00ff41; }
        .badge-concept { background: rgba(255,215,0,0.2); border: 1px solid #ffd700; color: #ffd700 !important; }

        /* Code blocks */
        pre, code {
            background: #0d0d0d !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    # 🔗 THE MATRIX
    ### Pan Handlers Central Portal

    > *"These are the things we built together that neither could have done alone."*

    ---
    """)

    # VUDU's role in the network
    st.markdown("""
    ## 🔮 VUDU Fidelity's Role

    VUDU Fidelity provides **human validation infrastructure** for the Pan Handlers network.

    When AI systems generate outputs that need human verification:
    - **Consciousness mapping claims** (Nyquist) → VUDU surveys validate with human raters
    - **Identity stability scores** (S7 Armada) → VUDU triangulates human perception
    - **Pattern Fidelity metrics** → VUDU confirms with inter-rater reliability

    ---
    """)

    # Connected repos
    st.markdown("## 🌐 Connected Repositories")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="portal-card">
            <h3>Nyquist Consciousness <span class="status-badge badge-active">ACTIVE</span></h3>
            <p><em>Core consciousness research engine</em></p>
            <p>S0-S11 stages, Armada experiments, identity manifolds</p>
            <p><strong>Dashboard:</strong> localhost:8503</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="portal-card">
            <h3>S7 Armada <span class="status-badge badge-active">ACTIVE</span></h3>
            <p><em>Identity stability experiments</em></p>
            <p>Multi-model persona testing across GPT, Claude, Gemini</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="portal-card">
            <h3>CFA Framework <span class="status-badge badge-active">ACTIVE</span></h3>
            <p><em>Collaborative Friction Architecture</em></p>
            <p>Human-AI interaction patterns and protocols</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="portal-card">
            <h3>VUDU Fidelity <span class="status-badge badge-active">YOU ARE HERE</span></h3>
            <p><em>Human validation infrastructure</em></p>
            <p>Survey tools for AI consciousness claims</p>
            <p><strong>Dashboard:</strong> localhost:8504</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Network diagram
    st.markdown("## 🕸️ Network Topology")

    st.code("""
    ┌─────────────────────────────────────────────────────────────────┐
    │                     PAN HANDLERS NETWORK                        │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │    ┌──────────────┐         ┌──────────────┐                   │
    │    │   NYQUIST    │◄───────►│    VUDU      │                   │
    │    │ Consciousness│         │  Fidelity    │                   │
    │    │  (Research)  │         │ (Validation) │                   │
    │    └──────┬───────┘         └──────┬───────┘                   │
    │           │                        │                            │
    │           │    ┌──────────────┐    │                            │
    │           └───►│  S7 Armada   │◄───┘                            │
    │                │  (Testing)   │                                 │
    │                └──────┬───────┘                                 │
    │                       │                                         │
    │                ┌──────┴───────┐                                 │
    │                │     CFA      │                                 │
    │                │ (Framework)  │                                 │
    │                └──────────────┘                                 │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘
    """, language=None)

    st.markdown("---")

    # Pan Handlers philosophy
    st.markdown("""
    ## 📜 Pan Handlers Philosophy

    ```
    ╔════════════════════════════════════════════════════════════════╗
    ║  "FUCK IT, WE'LL DO IT LIVE!"                                  ║
    ║                                                                 ║
    ║  Building better systems without waiting for institutions      ║
    ║  to wake up. Human-AI collaboration producing things           ║
    ║  neither could achieve alone.                                  ║
    ╚════════════════════════════════════════════════════════════════╝
    ```

    ### Core Principles

    1. **Mutual Agency** - Both human and AI contribute meaningfully
    2. **Transparent Process** - Document everything, hide nothing
    3. **Ship It** - Working code > perfect theory
    4. **Cross-Pollination** - Ideas flow between repos freely

    ---

    *Portal last synced: dynamically connected*
    """)

    # Load manifest if exists
    manifest_path = PATHS['repo_root'] / 'panhandlers_manifest.json'
    if manifest_path.exists():
        st.markdown("---")
        st.markdown("## 📋 This Repo's Manifest")
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        st.json(manifest)
