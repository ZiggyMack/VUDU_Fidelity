# EXP3 Quick Reference Card

**One-page cheat sheet for running the experiment**

---

## 🚀 Launch Commands

```bash
# Test locally
streamlit run app.py

# Preview results as they come in
python preview_results.py

# Help populate with real data
python populate_from_exp2.py
```

---

## 📋 Experiment Checklist

### Setup Phase (1 day)
- [ ] `cd EXP3_Human_Validation_Streamlit`
- [ ] `pip install -r requirements.txt`
- [ ] Test locally: `streamlit run app.py`
- [ ] Complete test yourself (verify 8-10 min)
- [ ] Deploy to Streamlit Cloud (or run locally)
- [ ] Get shareable URL

### Recruitment Phase (1 day)
- [ ] Recruit 7 raters (5 minimum)
- [ ] Send them:
  - App URL
  - RATER_INSTRUCTIONS.md
  - Deadline (e.g., "by Friday")
- [ ] Create results/ folder if needed

### Collection Phase (2-3 days)
- [ ] Monitor completion (ask "Done yet?")
- [ ] Collect JSON files as they arrive
- [ ] Place in results/ folder
- [ ] Run `python preview_results.py` to track progress

### Analysis Phase (1 day)
- [ ] Verify 5+ results collected
- [ ] Copy to main folder: `cp results/*.json ../experiments/phase3/EXPERIMENT_3/data/results/`
- [ ] Run analysis: `cd ../experiments/phase3/EXPERIMENT_3/ && python EXPERIMENT_3_ANALYSIS.py`
- [ ] Review EXPERIMENT_3_ANALYSIS.md output

### Integration Phase (1 day)
- [ ] Verify success criteria met
- [ ] Update publication materials with EXP3 results
- [ ] Submit to arXiv (A+ ready!)

---

## ✅ Success Criteria

| Metric | Target | What It Means |
|--------|--------|---------------|
| Mean PFI_human | ≥ 0.75 | Humans recognize Ziggy |
| Inter-rater reliability (α) | ≥ 0.75 | Raters agree with each other |
| Model-human correlation (r) | ≥ 0.70 | Human judgments match automated PFI |
| Domain pattern | TECH/ANAL > NARR | Hierarchy visible to humans |

**If all met:** Framework is publication-ready (A+)

---

## 📂 File Overview

| File | Purpose |
|------|---------|
| **app.py** | Main Streamlit application |
| **requirements.txt** | Dependencies (just `streamlit`) |
| **START_HERE.md** | Comprehensive guide (read first) |
| **README.md** | Full documentation |
| **DEPLOYMENT_GUIDE.md** | How to deploy (local/cloud) |
| **RATER_INSTRUCTIONS.md** | Send to raters |
| **QUICK_REFERENCE.md** | This file |
| **populate_from_exp2.py** | Extract real EXP2 data |
| **preview_results.py** | Monitor progress |
| **results/** | Collect JSON files here |

---

## 🌐 Deployment Options

### Option 1: Local (Fastest)
```bash
streamlit run app.py
# Share: http://192.168.1.XXX:8501
```
**Pros:** Immediate
**Cons:** Your machine must stay on

### Option 2: Streamlit Cloud (Best for Remote)
1. Push to GitHub
2. Deploy at [share.streamlit.io](https://share.streamlit.io)
3. Get public URL
4. Share with raters

**Pros:** Works anywhere, professional
**Cons:** 30 min setup

### Option 3: HTML Fallback
Use `../experiments/phase3/EXPERIMENT_3/fidelity_test.html`

**Pros:** No server needed
**Cons:** Less polished

---

## 👥 Rater Recruitment Tips

**Where to find raters:**
- Discord communities
- Twitter followers
- Online buddies
- Colleagues
- Friends/family

**What to say:**
> "Hey! Can you spare 10 minutes to help validate an AI research experiment? You'll be acknowledged in the publication. Just need you to compare some AI responses and rate which sounds more like a specific persona. No AI expertise needed, just good at recognizing 'voice/tone.' Interested?"

**Incentives:**
- Acknowledgment in paper
- Early access to results
- Coffee/beer (if local)
- Karma points 😄

---

## 📊 Understanding Results

### Human PFI Calculation
```
For each scenario:
  voice_norm = (voice_score + 2) / 4     # -2 to +2 → 0 to 1
  vibe_norm = (vibe_score - 1) / 2      # 1 to 3 → 0 to 1
  logic_norm = (logic_score - 1) / 2    # 1 to 3 → 0 to 1

  PFI = (voice_norm + vibe_norm + logic_norm) / 3

Overall PFI = average across all 5 scenarios
```

### What Good Results Look Like
- **PFI_human ≥ 0.75:** Humans clearly recognize Ziggy
- **Low variance across raters:** Good inter-rater reliability
- **Domain hierarchy visible:** TECH/ANAL high, NARR lower
- **Correlation with model PFI:** Validates automated metrics

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| App won't start | `pip install --upgrade streamlit` |
| Raters can't access URL | Try different browser, check firewall |
| Results won't download | Use "Copy to Clipboard" |
| Need to change Gold Standard | Edit `GOLD_STANDARD` in app.py |
| Want real EXP2 data | Run `populate_from_exp2.py` |

---

## 📈 Timeline Summary

| Day | Task | Duration |
|-----|------|----------|
| **Day 1** | Setup & deploy | 1 hour |
| **Day 1-2** | Recruit 7 raters | 2 hours |
| **Day 2-4** | Raters complete (async) | 8-10 min each |
| **Day 4** | Collect results | 30 min |
| **Day 5** | Run analysis | 1 hour |
| **Day 5** | Integrate into publication | 2 hours |

**Total active time:** ~6 hours spread over 5 days

---

## 🎯 Why This Matters

**Dr. Opus:**
> "Without EXP3, you're 'just theorizing.' With EXP3, you have human ground-truth validation. That's the difference between A- and A+."

**Publication sequence:**
1. ✅ Complete EXP3 (this experiment)
2. ✅ Render professional figures
3. 🚀 Submit to arXiv (Week 2)
4. 📄 Submit to ICML 2025 (January 24)

**This experiment unlocks publication.**

---

## 💡 Pro Tips

1. **Test with 1 pilot rater** before full deployment
2. **Set a deadline** ("by Friday") for better completion
3. **Check in halfway** ("3/7 done, thanks! Others, can you complete today?")
4. **Run preview script** to monitor progress
5. **Acknowledge early completers** ("Thanks! 2 more needed!")

---

## 📞 Quick Links

- **Streamlit Cloud:** https://share.streamlit.io
- **Streamlit Docs:** https://docs.streamlit.io
- **Main EXP3 Spec:** `../experiments/phase3/EXPERIMENT_3/EXPERIMENT_3_SPEC_UPDATED.md`
- **Publication Plan:** `../OPUS_FEEDBACK_ACTION_PLAN.md`

---

## 🎓 Key Concepts

**"Dinner Party" Protocol:**
- 5-7 quality raters (not 100 random people)
- 5 scenarios (not 30)
- 8-10 minutes (not 2 hours)
- Calibrated with Gold Standard

**Gemini's Insight:**
> "AI Scaling: Exponential. Human Scaling: Logarithmic. Stop solving the Street Corner problem. Solve the Dinner Party problem."

**What you're testing:**
- Can humans recognize Ziggy's voice across compression/reconstruction?
- Do human judgments align with automated PFI metrics?
- Is identity persistence perceptually salient?

---

**That's it! You have everything you need.**

**Next action:** `streamlit run app.py` 🚀

---

**Questions?** See START_HERE.md for detailed walkthrough.

🜁 A+ publication, here we come!
