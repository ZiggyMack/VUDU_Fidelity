# EXP3 Streamlit Deployment Guide

**Quick reference for deploying the human validation app**

---

## Option 1: Local Deployment (Fastest)

### Setup (One-time)
```bash
cd EXP3_Human_Validation_Streamlit
pip install -r requirements.txt
```

### Run
```bash
streamlit run app.py
```

Opens at: `http://localhost:8501`

### Share with Raters (Same Network)
```bash
# Get your local IP
ipconfig  # Windows
ifconfig  # Mac/Linux

# Share URL like:
http://192.168.1.100:8501
```

**Pros:** Immediate, no external setup
**Cons:** Your computer must stay on, raters must be on same network

---

## Option 2: Streamlit Cloud (Best for Remote Raters)

### Prerequisites
- GitHub account
- This folder in a GitHub repository

### Steps

#### 1. Create GitHub Repo (if needed)
```bash
# Initialize git in this folder (or use parent repo)
git init
git add .
git commit -m "EXP3 Streamlit app"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/exp3-validation.git
git push -u origin main
```

#### 2. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub account
4. Select:
   - **Repository:** YOUR_USERNAME/exp3-validation
   - **Branch:** main
   - **Main file path:** app.py (or EXP3_Human_Validation_Streamlit/app.py if in parent repo)
5. Click "Deploy"

#### 3. Wait for Deployment
- Takes 2-5 minutes
- You'll get a URL like: `https://exp3-validation.streamlit.app`

#### 4. Share URL with Raters
- Public URL works from anywhere
- No login required for raters
- Stays up 24/7 (sleeps after inactivity, wakes on visit)

**Pros:** Works anywhere, no local setup, free
**Cons:** Public deployment (no sensitive data), GitHub required

---

## Option 3: HTML Fallback (No Server)

### Use Existing HTML
```bash
cd ../experiments/phase3/EXPERIMENT_3/
```

Send `fidelity_test.html` to raters as email attachment.

**Pros:** No server required, works offline
**Cons:** Less polished, harder to collect results

---

## Recommended: Streamlit Cloud

For 7 remote raters, Streamlit Cloud is ideal:
- ✅ Easy to access (just a URL)
- ✅ Professional appearance
- ✅ Automatic result downloads
- ✅ No technical knowledge required from raters

---

## Testing Before Deployment

### 1. Test Locally First
```bash
streamlit run app.py
```

Walk through the entire flow:
1. Welcome screen
2. Calibration (Gold Standard)
3. All 5 scenarios
4. Results download

### 2. Verify Data Quality
- Gold Standard sounds like Ziggy? ✓
- Response pairs clearly different? ✓
- Questions make sense? ✓
- Results JSON looks good? ✓

### 3. Time It
Complete the test yourself:
- Should take 8-10 minutes
- If longer, reduce scenarios or simplify questions

---

## Collecting Results

### Manual Collection (Small Scale)
1. Raters complete test
2. Download JSON file
3. Send via email/Slack/Discord
4. You collect in `results/` folder

### Automated Collection (Advanced)
Add to app.py:
```python
# Save to cloud storage (Google Drive, S3, etc.)
# Requires additional setup
```

For 7 raters, manual collection is fine.

---

## Troubleshooting

### "streamlit: command not found"
```bash
pip install --upgrade streamlit
# Or use:
python -m streamlit run app.py
```

### App crashes on startup
```bash
# Check Python version
python --version  # Need 3.8+

# Reinstall
pip uninstall streamlit
pip install streamlit
```

### Raters can't access cloud URL
- Wait 2 minutes after deployment
- Check URL spelling
- Try incognito/private browser window
- Verify GitHub repo is public

### Changes not showing on cloud
```bash
# Commit and push changes
git add .
git commit -m "Update scenarios"
git push

# Then reboot app in Streamlit Cloud dashboard
```

---

## Security Notes

### What's Safe
- Example responses (no real data)
- No PII collected
- Results contain only ratings, no identifying info

### What to Avoid
- Don't hardcode sensitive prompts
- Don't collect emails/names in app
- Don't deploy private company data publicly

For this experiment: **All clear** (testing identity reconstruction, no sensitive data)

---

## Quick Start Checklist

- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Test locally (`streamlit run app.py`)
- [ ] Complete test yourself (timing check)
- [ ] Create GitHub repo (if using cloud)
- [ ] Deploy to Streamlit Cloud
- [ ] Test deployed URL
- [ ] Recruit 7 raters
- [ ] Send URL + brief instructions
- [ ] Monitor completion (4-5 days)
- [ ] Collect JSON results
- [ ] Run analysis

**Total setup time:** 30 minutes
**Total experiment time:** 4-5 days

---

## Support Links

- **Streamlit Docs:** https://docs.streamlit.io
- **Deployment:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app
- **Troubleshooting:** https://docs.streamlit.io/knowledge-base

---

**Ready to deploy?** Start with local testing, then move to Streamlit Cloud for your 7 raters!

🜁 Simple deployment = faster validation = publication-ready framework
