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

    # Matrix theme CSS - GREEN ON BLACK TERMINAL AESTHETIC (COMPLETE)
    st.markdown("""
        <style>
        /* ===== MATRIX THEME - GREEN ON BLACK TERMINAL AESTHETIC ===== */

        /* ===== BASE COLORS ===== */
        :root {
            --matrix-black: #0a0a0a;
            --matrix-dark: #0d0d0d;
            --matrix-green: #00ff41;
            --matrix-green-dim: #00cc33;
            --matrix-green-dark: #004d1a;
        }

        /* ===== BLACK BACKGROUND EVERYWHERE ===== */
        html, body,
        .stApp,
        .stApp > div,
        .stApp [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > div,
        .main,
        .main > div,
        .main .block-container,
        .block-container,
        [data-testid="stVerticalBlock"],
        [data-testid="stHorizontalBlock"],
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="column"],
        [data-testid="stElementContainer"] {
            background-color: #0a0a0a !important;
            background: #0a0a0a !important;
        }

        /* ===== ALL TEXT MATRIX GREEN ===== */
        .stApp p, .stApp span, .stApp div, .stApp label, .stApp li,
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
        .main p, .main span, .main div, .main label, .main li,
        .main h1, .main h2, .main h3, .main h4, .main h5, .main h6,
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stMarkdownContainer"] span,
        [data-testid="stMarkdownContainer"],
        p, span, div, li, label {
            color: #00ff41 !important;
        }

        /* ===== HEADERS ===== */
        h1, h2, h3, h4, h5, h6 {
            color: #00ff41 !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
        }

        h1 {
            border-bottom: 2px solid #00ff41;
            padding-bottom: 0.3em;
        }

        h2, h3 {
            border-bottom: 1px solid #00ff41;
            padding-bottom: 0.2em;
        }

        /* ===== BOLD TEXT WITH GLOW ===== */
        strong, b {
            color: #00ff41 !important;
            text-shadow: 0 0 5px rgba(0,255,65,0.5);
        }

        em, i {
            color: #00cc33 !important;
        }

        /* ===== LINKS ===== */
        a {
            color: #00cc33 !important;
        }
        a:hover {
            color: #00ff41 !important;
            text-shadow: 0 0 10px rgba(0,255,65,0.5);
        }

        /* ===== BLOCKQUOTES ===== */
        blockquote, blockquote p, blockquote span {
            color: #00cc33 !important;
            border-left: 3px solid #00ff41 !important;
            background: rgba(0,255,65,0.05) !important;
        }

        /* ===== HORIZONTAL RULES ===== */
        hr {
            border-color: #00ff41 !important;
            background-color: #00ff41 !important;
        }

        /* ===== LISTS ===== */
        ul, ol, li {
            color: #00ff41 !important;
        }

        /* ===== CODE BLOCKS ===== */
        code {
            background: rgba(0,255,65,0.1) !important;
            color: #00ff41 !important;
            font-family: 'Courier New', monospace !important;
        }

        pre, pre code,
        [data-testid="stCodeBlock"],
        .stCodeBlock,
        .stCodeBlock pre,
        .stCodeBlock code {
            background: #0d0d0d !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
            font-family: 'Courier New', monospace !important;
        }

        /* ===== TABLES ===== */
        th {
            background: #004d1a !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
        }

        td {
            color: #00ff41 !important;
            border-bottom: 1px solid #00ff41 !important;
            background-color: #0d0d0d !important;
        }

        /* ===== BUTTONS ===== */
        .stButton > button {
            background-color: #0d0d0d !important;
            color: #00ff41 !important;
            border: 2px solid #00ff41 !important;
            font-family: 'Courier New', monospace !important;
        }

        .stButton > button:hover {
            background-color: #004d1a !important;
            color: #ffffff !important;
            box-shadow: 0 0 15px rgba(0,255,65,0.4);
        }

        /* ===== INPUTS ===== */
        input, textarea, select,
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div {
            background-color: #0d0d0d !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
        }

        /* ===== EXPANDERS ===== */
        [data-testid="stExpander"] {
            background-color: #0d0d0d !important;
            border: 1px solid #00ff41 !important;
        }
        [data-testid="stExpander"] * {
            color: #00ff41 !important;
        }

        /* ===== JSON DISPLAY ===== */
        .stJson, .stJson * {
            background: #0d0d0d !important;
            color: #00ff41 !important;
        }

        /* ===== PORTAL CARDS ===== */
        .portal-card {
            background: linear-gradient(135deg, rgba(0,255,65,0.1) 0%, rgba(0,204,51,0.05) 100%) !important;
            border: 2px solid #00ff41 !important;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 0 20px rgba(0,255,65,0.2);
        }
        .portal-card:hover {
            box-shadow: 0 0 30px rgba(0,255,65,0.4);
        }
        .portal-card h3 {
            color: #00ff41 !important;
            margin-top: 0;
            border-bottom: none !important;
        }
        .portal-card p, .portal-card span, .portal-card em {
            color: #00cc33 !important;
        }
        .portal-card strong {
            color: #00ff41 !important;
        }

        /* ===== STATUS BADGES ===== */
        .status-badge {
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
        }
        .badge-active {
            background: rgba(0,255,65,0.2) !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
        }
        .badge-here {
            background: rgba(0,255,65,0.3) !important;
            color: #00ff41 !important;
            border: 1px solid #00ff41 !important;
            text-shadow: 0 0 5px rgba(0,255,65,0.5);
        }
        .badge-concept {
            background: rgba(255,215,0,0.2) !important;
            border: 1px solid #ffd700 !important;
            color: #ffd700 !important;
        }

        /* ===== METRICS ===== */
        [data-testid="stMetricValue"] {
            color: #00ff41 !important;
            font-family: 'Courier New', monospace !important;
        }
        [data-testid="stMetricLabel"] {
            color: #00cc33 !important;
        }

        /* ===== FINAL OVERRIDE ===== */
        .main .block-container * {
            color: #00ff41 !important;
        }
        .main .block-container strong, .main .block-container b {
            text-shadow: 0 0 5px rgba(0,255,65,0.5);
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
