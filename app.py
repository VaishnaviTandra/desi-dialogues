import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import uuid
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av
import tempfile

st.set_page_config(page_title="Desi Dialogues 🎙️", layout="centered")
st.title("🎭 Desi Dialogues – Voice the Drama!")
st.caption("Pick a Telugu dialogue, your region, and record how you'd say it in your slang.")

# ---- Load dialogues ----
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

# ---- Audio Recording ----
st.subheader("🎤 Record Your Voice")

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.frames = []
        self.sample_rate = None
        self.channels = None

    def recv_audio(self, frame: av.AudioFrame) -> av.AudioFrame:
        self.frames.append(frame)
        self.sample_rate = frame.sample_rate
        self.channels = frame.layout.channels
        return frame

ctx = webrtc_streamer(
    key="audio-recorder",
    mode=WebRtcMode.SENDONLY,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

# ---- Submit & Save ----
if st.button("Submit 🎉"):
    if dialogue and region and ctx.audio_processor and ctx.audio_processor.frames:
        os.makedirs("data", exist_ok=True)
        os.makedirs("audio", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save audio file as WAV
        audio_filename = f"{uuid.uuid4()}.wav"
        audio_path = os.path.join("audio", audio_filename)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            container = av.open(temp_file.name, mode="w", format="wav")
            stream = container.add_stream("pcm_s16le", rate=ctx.audio_processor.sample_rate or 48000)
            stream.channels = ctx.audio_processor.channels or 1
            for frame in ctx.audio_processor.frames:
                container.mux(frame)
            container.close()
            os.rename(temp_file.name, audio_path)

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

        st.audio(audio_path, format="audio/wav")
        st.success("✅ Your input and recording have been saved!")
    else:
        st.warning("⚠️ Please select all options and record your voice before submitting.")
