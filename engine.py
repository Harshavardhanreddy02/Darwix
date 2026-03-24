import pyttsx3
import math
import os
from transformers import pipeline

# Sophisticated pre-trained emotion classification [cite: 39]
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=3)

def synthesize_vocal_output(text: str):
    raw = emotion_analyzer(text)[0]
    emotion = raw[0]['label']
    confidence = raw[0]['score']

    # Negation Handling Logic
    if any(n in text.lower().split() for n in ["not", "no", "never"]):
        if emotion in ["anger", "fear", "sadness"]: 
            emotion, confidence = "neutral", 0.5

    intensity = math.sqrt(confidence)
    
    # Emotion-to-Voice Mapping [cite: 24]
    profiles = {
        "joy": {"rate": 180, "volume": 0.9, "pitch": 180},
        "sadness": {"rate": 110, "volume": 0.5, "pitch": 60},
        "anger": {"rate": 200, "volume": 1.0, "pitch": 130},
        "neutral": {"rate": 160, "volume": 0.8, "pitch": 120}
    }
    base = profiles.get(emotion, profiles["neutral"])
    
    # Programmatic Parameter Modulation [cite: 17]
    params = {
        "rate": int(base["rate"] + (intensity * 30)),
        "volume": round(min(base["volume"] + (intensity * 0.3), 1.0), 2),
        "pitch": base["pitch"]
    }

    engine = pyttsx3.init() # Offline TTS [cite: 41]
    if os.path.exists("output.mp3"): os.remove("output.mp3")
    engine.setProperty('rate', params['rate'])
    engine.setProperty('volume', params['volume'])
    engine.save_to_file(text, "output.mp3")
    engine.runAndWait()
    engine.stop()
    
    return {"emotion": emotion, "intensity": round(intensity, 2), "params": params}