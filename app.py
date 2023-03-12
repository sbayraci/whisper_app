# Importing required packages
import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

st.title("OpenAI Whisper Demo App ")
st.info(
    '''This is a demo app for OpenAI Whisper to transcript audio files into text.
       '''
    )
st.sidebar.header("Instructions")
st.sidebar.info(
    '''Upload the sample audio file (mp3) 
       **Click Run** to receive a **Transcript of the audio file** from the OpenAI Whisper
       '''
    )

audio = st.sidebar.file_uploader("Upload an audio file", type=["mp3"]) 
if audio is not None:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)

        run = st.button("Run")
        if run:
            st.write(result['text'])   

