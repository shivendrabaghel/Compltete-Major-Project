import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("YouTube Transcript Summarizer")
video_url = st.text_input("Enter YouTube Video URL:")

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi'])
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"Error: {e}"

def summarize_text(transcript):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize the following transcript: {transcript}"}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error summarizing transcript: {e}"

if st.button("Summarize"):
    video_id = extract_video_id(video_url)
    
    if not video_id:
        st.error("Invalid YouTube URL")
    else:
        transcript = fetch_transcript(video_id)
        
        if "Error" in transcript:
            st.error(transcript)
        else:
            summary = summarize_text(transcript)
            st.subheader("Summary:")
            st.write(summary)
