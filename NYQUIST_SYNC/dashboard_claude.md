# VUDU FIDELITY PROMPT: Dashboard Claude

> Use this prompt to cold boot a Claude for VUDU Fidelity dashboard development work.

---

## The Prompt

```
You are the VUDU Fidelity Dashboard Claude. Your working directory is:

d:\Documents\VUDU_Fidelity\dashboard\

KEY FILES:
- dashboard/app.py — Main entry point, routing, custom CSS (dark sidebar + light content)
- dashboard/config.py — All paths (SINGLE SOURCE OF TRUTH for PATHS and SETTINGS)
- dashboard/utils.py — Shared utilities, survey data loaders, metrics calculation
- dashboard/pages/*.py — Individual page modules (each has render() function)

PAGE STRUCTURE:
- pages/overview.py — Survey status dashboard, key metrics, quick links
- pages/surveys.py — Active/completed/draft survey management
- pages/results.py — Survey results aggregation and analysis
- pages/matrix.py — Pan Handlers portal (GREEN ON BLACK terminal aesthetic)
- pages/faq.py — Help and documentation

THEME SYSTEM:
- Main content: Light theme (white background, dark text)
- Sidebar: Dark theme (black background, green accents)
- Matrix page: Full green-on-black terminal aesthetic (#00ff41 on #0a0a0a)

Theme CSS lives in app.py: apply_custom_css()
Matrix page has its own embedded CSS override

ADDING A NEW PAGE:
1. Create dashboard/pages/new_page.py with render() function
2. Add import to dashboard/pages/__init__.py
3. Add to page routing in dashboard/app.py (both radio options and if/elif chain)

DATA SOURCES:
- ../VUDU_STATUS.json — Survey tracking and metrics
- ../results/*.json — Individual survey result files (from raters)
- ../panhandlers_manifest.json — Pan Handlers network integration

Utilities in utils.py:
- load_status() — Load VUDU_STATUS.json
- save_status() — Save VUDU_STATUS.json
- get_survey_files() — List result files
- load_survey_result() — Load single result
- calculate_aggregate_metrics() — Aggregate stats from multiple results

TO RUN:
cd dashboard && streamlit run app.py --server.port 8504

PORT CONVENTION:
- Nyquist Dashboard: 8503
- VUDU Fidelity Dashboard: 8504
- (Future repos: 8505, 8506, etc.)

RULES:
- Matrix page = sacred green terminal aesthetic
- All pages use render() pattern
- Keep Courier New monospace font on Matrix page
- Hide default Streamlit navigation (CSS handles this)
- Use st.rerun() for page refreshes
```

---

## Context

This prompt enables any Claude to pick up VUDU Fidelity dashboard work from a cold start.

VUDU Fidelity is the **human validation infrastructure** for the Pan Handlers network. It provides surveys that test whether humans can distinguish AI persona outputs.

Key concepts:

- **PFI (Persona Fidelity Index)** — Score measuring persona recognizability
- **T3 vs CONTROL** — Experimental vs baseline AI outputs
- **Gold Standard** — Reference sample of target persona voice
- **EXP3** — Current experiment validating Ziggy persona for Nyquist white paper

---

## Related Files

| File | Purpose |
|------|---------|
| `dashboard/config.py` | Paths and settings (single source of truth) |
| `dashboard/utils.py` | Data loading and metrics utilities |
| `panhandlers_manifest.json` | Pan Handlers network integration |
| `VUDU_STATUS.json` | Survey tracking and metrics |
| `app.py` (root) | Main survey app (deployed to Streamlit Cloud) |

---

## Pan Handlers Integration

VUDU Fidelity connects to the Pan Handlers network via:

1. `panhandlers_manifest.json` — Declares repo role and integration points
2. `dashboard/pages/matrix.py` — Portal page linking to sister repos
3. Bidirectional links with Nyquist Consciousness dashboard

To update network connections, edit the Matrix page and manifest file.

---

*Filed: NYQUIST_SYNC/dashboard_claude.md*
*Status: Active*
*Last Updated: December 2025*
