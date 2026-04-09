# Empathy Engine: Emotion-Aware Text-to-Speech System

## Project Description
Empathy Engine converts text into expressive speech by detecting emotion and modulating voice parameters. It combines an AI sentiment model with simple rules to keep speech human-like and responsive.

## Features
- Text input processing
- Transformer-based emotion detection (Hugging Face `pipeline`)
- Granular emotion mapping (Happy, Angry, Positive, Negative, Neutral)
- Intensity-based speech rate adjustment
- Real-time voice playback (CLI via `pyttsx3`, web via gTTS audio file)
- Audio file generation (`static/output.mp3`)
- Flask web interface (new)

## How It Works
```
Text Input
   ↓
Emotion Detection (Transformer Model)
   ↓
Granular Emotion Logic
   ↓
Intensity Scaling
   ↓
Voice Parameter Mapping (Rate)
   ↓
Speech Output + Audio File
```

## Tech Stack
- Python
- Hugging Face Transformers
- pyttsx3 (CLI voice)
- gTTS (MP3 generation)
- Flask (web UI)

## Installation

### 1. Clone the repository
git clone https://github.com/your-username/empathy-engine.git

### 2. Navigate to project folder
cd empathy-engine

### 3. Create virtual environment (optional but recommended)
python -m venv .venv

### 4. Activate virtual environment
Windows:
.venv\Scripts\activate

### 5. Install dependencies
pip install -r requirements.txt

### 6. Run the project
python main.py

## Setup Instructions
1) Clone and enter the project
```
git clone <your-repo-link>
cd empathy-engine
```

2) Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
```

3) Install dependencies
```
pip install textblob gtts pyttsx3 transformers torch flask
```

## Run the CLI app
```
python main.py
```
Enter text in the terminal to hear spoken output and save `output.mp3`.

## Run the Flask web UI
```
python app.py
```
Open http://127.0.0.1:5000 in your browser. The first request may download the sentiment model—wait until it finishes. Submit text to see:
- Detected emotion with confidence
- Derived speech rate
- Audio player streaming `static/output.mp3`

## Usage Flow (web)
1. Type text in the textarea
2. Click **Generate Voice**
3. Page reloads showing the input, detected emotion, confidence, speech rate, and an audio player

## Web UI Snapshot
The UI (dark gradient card) mirrors the Text → Emotion → Voice → Audio flow. It centers the form and results, shows your submitted text, emotion, confidence, speech rate, and provides an audio player for the generated file. The primary action is the “Generate Voice” button; results appear immediately below.

## Example
**Input:** `I am very happy today!`

**Output:**
- Emotion: Positive / Happy
- Faster speech rate
- Generated audio file

## Design Decisions
1) Emotion detection upgraded from TextBlob to a transformer for better context.
2) Keyword overrides improve granularity (`happy` → Happy, `angry` → Angry).
3) Confidence score drives speech rate (stronger confidence → larger adjustment).
4) Speech-rate mapping: Positive/Happy = faster, Negative/Angry = slower, Neutral = baseline.

## Limitations
- Keyword overrides are simple.
- Only rate is modulated (pitch unchanged).
- gTTS needs internet access.

## Future Improvements
- Expand emotion set (e.g., surprise, concern).
- Integrate richer TTS services (Google Cloud, ElevenLabs).
- Fine-tune emotion model for domain data.

## Author
Dinesh
