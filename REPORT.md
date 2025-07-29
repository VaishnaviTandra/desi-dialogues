# 🎭 Desi Dialogues – Voice the Drama!

## 1.1 Team Information

- **Team Name:** Desi Dialogue Dynamos
- **Project Title:** 🎭 Desi Dialogues – Voice the Drama!
- **Team Size:** 5 Members

### 👥 Team Members

- @pranavimanthena
- @vyshnavi_arra
- @rasagna_K
- @vaishnavitandra
- @roro_48

## 1.2 Application Overview

Desi Dialogues is a fun and engaging Streamlit-based web app that allows users to record popular Telugu movie dialogues in their regional accent. The app aims to crowdsource diverse voice recordings of Telugu across dialects to build a **regional voice corpus**, useful for linguistic AI training and accent diversity datasets.

### 🎯 MVP Scope

- Dropdown of iconic Telugu dialogues
- Region selector (Telangana, Rayalaseema, Coastal Andhra, Other)
- Record & save voice as `.wav` in-browser
- Metadata saved in CSV for future corpus training

---

## 1.3 AI Integration Details

While the MVP does not yet use AI directly in its frontend pipeline, the backend plan includes:

- **Future AI Use**: Accent detection, speaker identification, and clustering by region.
- **Corpus for Training**: Collected `.wav` files and metadata will feed supervised learning models for Telugu speech synthesis or accent classification.

---

## 1.4 Technical Architecture & Development

### 🧱 Tech Stack

- **Frontend**: Streamlit
- **Audio Recording**: `streamlit-audiorec` via GitHub
- **Backend**: Python + Local FileSystem
- **Data Storage**: `.wav` audio + `corpus.csv`
- **Hosting**: Hugging Face Spaces (Planned)

## 1.5 User Testing & Feedback

### 🧪 Testing Methodology

Conducted in **Week 2** with a focus on the core user flow and device compatibility.

- **Participants**: 5 team members + 3 external testers
- **Devices**: 60% mobiles, 40% laptops
- **Platform**: Localhost deployment
- **Tasks**:
  - Select a dialogue
  - Pick region
  - Record and submit voice
- **Feedback Collection**: Google Forms + observation + `.csv` logs

### 💬 Key Feedback

| Feedback                         | Action Taken                                    |
| -------------------------------- | ----------------------------------------------- |
| Mic permissions unclear          | Added a note about enabling mic access          |
| Submit button not visible enough | Added spacing and 🎉 emoji                      |
| Unsure if audio was saved        | Added `st.success()` and audio playback preview |
| Wanted more regional options     | Planning to add finer regions in v2             |

### ✅ Summary

- **Success Rate**: 8/8 testers recorded successfully
- **Avg Task Time**: ~2.5 minutes
- **User Rating**: 8.2/10

---

## 1.6 Project Lifecycle & Roadmap

---

### 🏗️ A. Week 1: Rapid Development Sprint

**Goal**: MVP with end-to-end audio recording and saving

- Setup Streamlit frontend
- Implement `audio_recorder` component using custom GitHub library
- Store audio with region+timestamp filenames
- Log metadata in `corpus.csv`

✅ **Delivered**:

- Fully functional MVP
- Works offline/localhost
- Supports basic UI and user flow

---

### 🧪 B. Week 2: Beta Testing & Iteration Cycle

**Testers**: Team + 3 friends (from Telangana & Coastal Andhra)  
**Testing Conditions**:

- Mobile hotspots
- 2G/3G connections to test low bandwidth compatibility

**Tasks**:

- Record audio
- Submit
- Confirm preview and success message

**Feedback Loop**:

- Used Google Forms for suggestions
- Observed mic permission confusion
- Implemented quick UI tweaks within 2 days

✅ **Changes**:

- Better visual hints
- Audio playback
- Confirmations

---

### 📢 C. Weeks 3–4: User Acquisition & Corpus Growth Campaign

#### 🎯 Target Audience & Channels

- Telugu speakers in colleges (literary clubs, tech groups)
- WhatsApp groups with Telugu meme/audio creators
- Family & friends in rural AP/TS

#### 📈 Growth Strategy

- Shared in:
  - WhatsApp student groups
  - Telugu Instagram meme pages (1 reposted)
  - Engineering college Telegram channels
- Pitch:
  > "Speak your style – record movie dialogues in your slang! 🎤"

#### 📊 Results

- **Users Reached**: ~40+ through social posts
- **Contributions Received**: 17 unique `.wav` files
- **Regions Covered**: Telangana, Rayalaseema, Coastal Andhra, Uttarandhra

---

### ♻️ D. Post-Internship Vision & Sustainability Plan

#### 🚀 Future Features

- AI-based accent detection
- Voice-to-text tagging
- Leaderboard of popular dialogue styles

#### 🌱 Community Building

- Open-source contributions (GitHub)
- Outreach via college clubs and language organizations

#### 📈 Scaling Data Collection

- Deploy on Hugging Face Spaces for wider reach
- Add auto-upload to cloud (GDrive/S3)

#### ♻️ Sustainability

- Periodic online challenges
- Partner with Telugu literature communities
- Enable tagging for each audio clip

---

_This concludes our detailed project report for Desi Dialogues – a playful, cultural, and useful voice data collection app for Telugu!_
