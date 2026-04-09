from transformers import pipeline
from gtts import gTTS
import pyttsx3

# Load AI model
classifier = pipeline("sentiment-analysis")

# 1. Take input
text = input("Enter your text: ")
text_lower = text.lower()

# 2. Emotion detection (AI)
result = classifier(text)[0]
label = result['label']
score = result['score']   # used for intensity

# 3. Granular Emotion (override basic emotion)
if "angry" in text_lower:
    emotion = "Angry"
elif "happy" in text_lower:
    emotion = "Happy"
else:
    if label == "POSITIVE":
        emotion = "Positive"
    elif label == "NEGATIVE":
        emotion = "Negative"
    else:
        emotion = "Neutral"

print("Emotion:", emotion)
print("Confidence Score:", score)

# 4. Intensity Scaling (MAIN UPGRADE)
if emotion in ["Positive", "Happy"]:
    rate = 160 + int(score * 60)
elif emotion in ["Negative", "Angry"]:
    rate = 160 - int(score * 60)
else:
    rate = 160

print("Rate:", rate)

# 5. Text-to-Speech (voice)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', rate)

engine.say(text)
engine.runAndWait()

# 6. Save audio file
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

print("Audio saved as output.mp3")