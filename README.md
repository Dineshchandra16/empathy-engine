# Empathy Engine
Emotion-aware text-to-speech that turns text into expressive audio in one click.

## Overview
Empathy Engine detects the emotional tone of text with a transformer model, applies simple overrides for key feelings (happy/angry), scales speech rate by confidence, and generates an MP3 you can play instantly in the browser or via CLI.

## Quickstart (Web UI)
```bash
git clone https://github.com/your-username/empathy-engine.git
cd empathy-engine
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 and submit text. First run may download the sentiment model—wait for it to finish.

## Requirements
- Python 3.10+ recommended
- Internet access for first model download and gTTS synthesis

## Installation (detailed)
1. Clone: `git clone https://github.com/your-username/empathy-engine.git`
2. Enter folder: `cd empathy-engine`
3. Create venv (recommended): `python -m venv .venv`
4. Activate (Windows): `.venv\Scripts\activate`
5. Install deps: `pip install -r requirements.txt`

## Run
- CLI demo: `python main.py` (prompts in terminal, saves `output.mp3`)
- Flask web UI: `python app.py` (serves `static/output.mp3` for playback)

## Usage Flow (web)
1. Type text in the textarea
2. Click **Generate Voice**
3. Page reloads showing input, detected emotion, confidence, derived speech rate, and an audio player streaming `static/output.mp3`

## Features
- Transformer-based sentiment via `pipeline("sentiment-analysis")`
- Keyword overrides: “happy” → Happy, “angry” → Angry
- Intensity-based speech rate mapping:
  - Positive/Happy: `160 + int(score * 60)`
  - Negative/Angry: `160 - int(score * 60)`
  - Neutral: `160`
- gTTS MP3 generation served from `/static/output.mp3`
- Lightweight Flask UI with centered dark card layout

## Architecture (concept)
```
Text → Sentiment Model → Granular Emotion → Intensity Scaling → Rate Mapping → gTTS → output.mp3 → Browser Audio
```

## UI Preview
Dark gradient card with textarea, primary “Generate Voice” button, analysis block (emotion, confidence, speech rate), and embedded audio player reflecting the generated file.

## Troubleshooting
- Model download slow on first run: wait for completion, then refresh.
- No audio: ensure `static/output.mp3` exists (generated after first POST).
- gTTS requires internet; check connectivity if synthesis fails.

## Roadmap
- Broader emotion set (surprise, concern, etc.)
- Pitch modulation in addition to rate
- Optional cloud TTS backends (e.g., Google, ElevenLabs)

## Author
Dinesh
