# 🎭 Desi Dialogues – Voice the Drama!

A fun and engaging Streamlit app where users pick a famous Telugu movie dialogue and record it in their own **regional slang or accent**. The goal is to collect a **voice corpus of diverse spoken Telugu** from different regions of Andhra Pradesh and Telangana.

---

## 📌 Project Objective

To create a low-bandwidth, offline-friendly voice data collection app that:

- Encourages cultural expression through dialogue mimicry.
- Collects `.wav` audio data from Telugu speakers.
- Builds a speech corpus for future **AI-driven linguistic research** (accent detection, TTS, ASR, etc.).

---

## 💡 Features

- 🎬 Dropdown of famous Telugu movie dialogues
- 🌍 Region selection: Telangana, Rayalaseema, Coastal Andhra, Other
- 🎤 Voice recording directly in the browser
- 💾 Corpus stored as `.wav` + metadata in `corpus.csv`
- ✅ User feedback and audio preview after recording
- ⚡ Works offline (localhost), planned deployment on Hugging Face Spaces

---

## 🛠 Tech Stack

| Layer       | Technology                              |
| ----------- | --------------------------------------- |
| Frontend    | Streamlit                               |
| Audio Input | `streamlit-audiorec` (custom component) |
| Backend     | Python + Local Files                    |
| Storage     | `.wav` files + `corpus.csv`             |
| Deployment  | Hugging Face Spaces (planned)           |

---

## 🚀 How to Run the App

### Prerequisites

- Python 3.8+
- `pip`

### Install Dependencies

```bash
pip install -r requirements.txt
streamlit run app.py
```

⚠️ If you see “streamlit not found”, try restarting the terminal or running:

```bash
python -m streamlit run app.py
```

### 🧠 AI Integration (Planned)

Accent detection using AI models
Speaker clustering by region
Speech-to-text with regional accuracy
Training dataset for Telugu TTS/ASR models

### 🤝 Contributing

We welcome contributions! See CONTRIBUTING.md for guidelines.

### 📄 License

This project is licensed under the MIT License.

### 🙏 Acknowledgements

Developed as part of Viswam.AI Corpus Collection Challenge
Inspired by Telugu cinema and regional language richness
Thanks to all testers and contributors who added their voice 🎤
