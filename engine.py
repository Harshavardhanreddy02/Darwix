import pyttsx3
import math
import os
from transformers import pipeline

# Optimized Sentiment Model Loader
# Downloads the RoBERTa model for high-accuracy emotion detection
emotion_analyzer = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=3 
)

def extract_vocal_tone(input_text: str):
    """
    Analyzes text to determine primary emotion with a 
    custom override for negation (e.g., 'not angry').
    """
    raw_predictions = emotion_analyzer(input_text)[0]
    sorted_data = sorted(raw_predictions, key=lambda x: x['score'], reverse=True)
    
    primary_emotion = sorted_data[0]['label']
    confidence_score = sorted_data[0]['score']

    # --- NEGATION OVERRIDE LOGIC ---
    # This prevents the AI from getting tricked by 'not angry' or 'not sad'
    negation_tokens = ["not", "no", "never", "don't", "isnt", "wasnt", "arent"]
    words = input_text.lower().split()
    
    has_negation = any(neg in words for neg in negation_tokens)
    
    if has_negation:
        # If the model detects a strong emotion but the user used a negation word,
        # we pull the emotion back to 'neutral' for more accurate synthesis.
        if primary_emotion in ["anger", "fear", "disgust", "sadness"]:
            primary_emotion = "neutral"
            confidence_score = 0.5  # Calm down the intensity

    # Square root scaling for smoother intensity transitions
    dynamic_intensity = math.sqrt(confidence_score)

    return primary_emotion, dynamic_intensity, sorted_data

def define_vocal_profile(emotion: str):
    """
    Mapping emotions to specific vocal frequency and speed presets.
    """
    VOCAL_PROFILES = {
        "joy":      {"rate": 175, "volume": 0.9, "pitch": 180},
        "sadness":  {"rate": 115, "volume": 0.5, "pitch": 70},
        "anger":    {"rate": 195, "volume": 1.0, "pitch": 130},
        "fear":     {"rate": 145, "volume": 0.7, "pitch": 95},
        "surprise": {"rate": 210, "volume": 1.0, "pitch": 170},
        "neutral":  {"rate": 165, "volume": 0.8, "pitch": 125}
    }
    return VOCAL_PROFILES.get(emotion, VOCAL_PROFILES["neutral"])

def calculate_modulations(emotion: str, intensity: float):
    """
    Calculates final rate, volume, and pitch based on emotional intensity.
    """
    profile = define_vocal_profile(emotion)
    R_VAR, V_VAR, P_VAR = 40, 0.4, 70

    # Rate modulation
    if emotion == "sadness":
        final_rate = int(profile["rate"] - (intensity * 30))
    else:
        final_rate = int(profile["rate"] + (intensity * R_VAR))

    # Volume modulation (maxed at 1.0)
    final_volume = min(profile["volume"] + (intensity * V_VAR), 1.0)

    # Pitch modulation (OS dependent)
    if emotion in ["joy", "surprise"]:
        final_pitch = int(profile["pitch"] + (intensity * P_VAR))
    elif emotion == "sadness":
        final_pitch = int(profile["pitch"] - (intensity * P_VAR))
    else:
        final_pitch = int(profile["pitch"] + (intensity * (P_VAR / 2)))

    return {
        "rate": final_rate,
        "volume": round(final_volume, 2),
        "pitch": final_pitch
    }

def create_audio_file(text: str, settings: dict, output_name: str = "output.mp3"):
    """
    Generates the audio file using the system TTS engine.
    """
    voice_engine = pyttsx3.init()

    voice_engine.setProperty('rate', settings['rate'])
    voice_engine.setProperty('volume', settings['volume'])

    try:
        voice_engine.setProperty('pitch', settings['pitch'])
    except Exception:
        pass 

    # Refresh file to avoid write-locks
    if os.path.exists(output_name):
        os.remove(output_name)

    voice_engine.save_to_file(text, output_name)
    voice_engine.runAndWait()
    voice_engine.stop() # Properly shut down the engine loop
    
    return output_name

def synthesize_vocal_output(text: str):
    """
    Main entry point for the text-to-speech pipeline.
    """
    emotion, intensity, raw_output = extract_vocal_tone(text)
    vocal_settings = calculate_modulations(emotion, intensity)
    audio_path = create_audio_file(text, vocal_settings)

    return {
        "emotion": emotion,
        "intensity": round(intensity, 2),
        "voice_params": vocal_settings,
        "audio_file": audio_path,
        "metadata": raw_output
    }