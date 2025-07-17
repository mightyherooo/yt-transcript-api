from flask import Flask, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

app = Flask(__name__)

# ✅ Allow only your frontend URL
CORS(app, origins=["https://youtubescribe.pages.dev"])

@app.route("/")
def home():
    return "YouTube Transcript API is running."

@app.route("/transcript/<video_id>")
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["sl", "en"])
        return jsonify(transcript)
    except NoTranscriptFound:
        return jsonify({"error": "Transcript not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
