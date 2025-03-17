from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        transcript = fetch_transcript(video_id)

        if "Error" not in transcript:
            transcript = summarize_with_gemini(transcript)  # Summarize transcript
    
    return render_template("template.html", transcript=transcript)

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return "Invalid YouTube URL"

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi'])
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"Error fetching transcript: {e}"

def summarize_with_gemini(transcript):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct model
        response = model.generate_content(f"Summarize this transcript: {transcript}")
        return response.text
    except Exception as e:
        return f"Error summarizing transcript: {e}"

if __name__ == "__main__":
    app.run(debug=True)
