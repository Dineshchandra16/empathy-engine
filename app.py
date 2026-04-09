"""Flask web interface for the Empathy Engine.

The app accepts text, detects emotion with a transformer pipeline,
scales speech rate based on intensity, generates speech with gTTS,
and serves the resulting audio for playback in the browser.
"""

import os
from flask import Flask, render_template, request
from transformers import pipeline
from gtts import gTTS


app = Flask(__name__)

# Configure where the generated audio is stored (served via /static/output.mp3)
AUDIO_PATH = os.path.join(app.root_path, "static", "output.mp3")

# Load the sentiment analysis pipeline once at startup
classifier = pipeline("sentiment-analysis")


def detect_emotion(text: str):
    """Return (emotion_label, score) using model with keyword overrides."""
    result = classifier(text)[0]
    label = result["label"]
    score = result["score"]
    lowered = text.lower()

    if "angry" in lowered:
        emotion = "Angry"
    elif "happy" in lowered:
        emotion = "Happy"
    elif label == "POSITIVE":
        emotion = "Positive"
    elif label == "NEGATIVE":
        emotion = "Negative"
    else:
        emotion = "Neutral"

    return emotion, score


def speech_rate(emotion: str, score: float) -> int:
    """Map emotion and intensity to speech rate."""
    if emotion in ["Positive", "Happy"]:
        return 160 + int(score * 60)
    if emotion in ["Negative", "Angry"]:
        return 160 - int(score * 60)
    return 160


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    result = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            message = "Please enter some text to analyze."
        else:
            emotion, score = detect_emotion(text)
            rate = speech_rate(emotion, score)

            # Generate the audio file; overwrite if it already exists
            tts = gTTS(text=text, lang="en")
            tts.save(AUDIO_PATH)

            result = {
                "text": text,
                "emotion": emotion,
                "score": round(score, 3),
                "rate": rate,
            }

    audio_exists = os.path.exists(AUDIO_PATH)
    return render_template(
        "index.html", result=result, message=message, audio_exists=audio_exists
    )


if __name__ == "__main__":
    app.run(debug=True)
