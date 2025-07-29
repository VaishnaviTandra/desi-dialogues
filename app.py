import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from streamlit_audio_recorder.st_audiorec import st_audiorec
import uuid

st.set_page_config(page_title="Desi Dialogues 🎙️", layout="centered")
st.title("🎭 Desi Dialogues – Voice the Drama!")
st.caption("Pick a Telugu dialogue, your region, and record how you'd say it in your slang.")

# Load dialogues
with open("dialogues.json", "r", encoding="utf-8") as f:
    dialogues = json.load(f)

dialogue = st.selectbox("🗣️ Select a Telugu Movie Dialogue", dialogues)
region = st.selectbox(
    "🌍 Select Your Region",
    [
        "Telangana",
        "Rayalaseema",
        "Coastal Andhra",
        "Uttarandhra (North Coastal)",
        "Godavari Region",
        "Guntur/Palnadu",
        "Nellore/Prakasam",
        "Hyderabad Mix",
        "Other / NRI Telugu"
    ]
)

# Removed text area for user input
# st.subheader("✍️ Type Your Dialogue")
# user_input = st.text_area("Enter how you'd say the dialogue in your slang:")

st.subheader("🎤 Record Your Voice")
audio_data = st_audiorec()

if audio_data is not None:
    st.audio(audio_data, format='audio/wav')

if st.button("Submit 🎉"):
    if dialogue and region and audio_data is not None:
        os.makedirs("data", exist_ok=True)
        os.makedirs("audio", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Save audio file
        audio_filename = f"{uuid.uuid4()}.wav"
        audio_path = os.path.join("audio", audio_filename)
        with open(audio_path, "wb") as f:
            f.write(audio_data)
        # Save metadata to CSV
        row = {
            "Dialogue": dialogue,
            "Region": region,
            "Timestamp": timestamp,
            "AudioFile": audio_filename
        }
        csv_path = "data/corpus.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])
        df.to_csv(csv_path, index=False)
        st.success("✅ Your input and recording have been saved!")
    else:
        st.warning("⚠️ Please select all options and record your voice before submitting.")
