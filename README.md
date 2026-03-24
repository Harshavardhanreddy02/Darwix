# 🎙️ VocalSync AI: The Empathy Engine

## 📌 Project Overview

**VocalSync AI** is an advanced Text-to-Speech (TTS) system that transforms plain text into expressive speech by dynamically adapting voice characteristics based on detected emotions and their intensity.

Unlike traditional TTS systems, VocalSync AI bridges the gap between robotic output and human-like expression by incorporating **emotion detection**, **context awareness**, and **voice modulation**.

---

## 🚀 Key Features

* 🧠 **Context-Aware Emotion Detection**
  Uses a transformer-based model to classify text into nuanced emotional states.

* 🔍 **Smart Negation Handling**
  Detects negation words (e.g., *not*, *never*) to avoid incorrect emotion interpretation.

* 📊 **Dynamic Intensity Scaling**
  Applies smooth scaling (square-root based) to avoid abrupt emotional transitions.

* 🔊 **Emotion-Based Voice Modulation**
  Adjusts:

  * Speech Rate
  * Pitch
  * Volume

* 🌐 **End-to-End Pipeline**
  **Text → Emotion → Audio**

* 🎨 **Modern UI (Glassmorphism)**
  Clean and responsive interface using FastAPI + Jinja2.

---

## 🛠 Tech Stack

* **Language:** Python
* **Backend:** FastAPI
* **NLP Model:** HuggingFace Transformers
* **TTS Engine:** pyttsx3
* **Frontend:** HTML (Jinja2 Templates)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
project/
│── engine.py          # Emotion detection + TTS logic
│── main.py            # FastAPI application
│── templates/
│     └── index.html   # UI
│── requirements.txt
```

---

## 🧠 Core Design & Logic

### 1️⃣ Emotion Detection

Model Used:

```
j-hartmann/emotion-english-distilroberta-base
```

* Outputs probability distribution across emotions:

  * Joy, Sadness, Anger, Fear, Surprise, Disgust, Neutral

---

### 2️⃣ Intensity Calculation

We calculate emotional intensity as:

```
Intensity = Top Score − Second Top Score
```

✅ **Why this approach?**

* Captures confidence gap
* Reduces ambiguity
* More stable than raw probability

---

### 3️⃣ Emotion → Voice Mapping

| Emotion  | Rate      | Volume | Pitch  |
| -------- | --------- | ------ | ------ |
| Joy      | High      | High   | High   |
| Sadness  | Low       | Low    | Low    |
| Anger    | High      | High   | Medium |
| Fear     | Medium    | Medium | Low    |
| Surprise | Very High | High   | High   |
| Neutral  | Medium    | Medium | Medium |

---

### 4️⃣ Intensity-Based Modulation

Voice parameters dynamically adapt:

* **Rate**

  * Faster → Joy, Anger
  * Slower → Sadness

* **Volume**

  * Scales with intensity (max capped at 1.0)

* **Pitch**

  * Higher → Joy, Surprise
  * Lower → Sadness

---

## 📌 Example

**Input:**

```
"I am very happy today because I got a job!"
```

**Output:**

* Emotion: **Joy**
* Intensity: **High**
* Voice: **Fast, energetic, high-pitch**

---

## ⚠️ Limitations

* pyttsx3 has limited pitch control (OS-dependent)
* Less realistic compared to modern APIs (e.g., ElevenLabs)
* No speaker consistency or advanced prosody modeling

---

## 🔮 Future Improvements

* 🔊 Integrate ElevenLabs / Google TTS
* ⚡ Real-time audio streaming
* 🧠 Improved contextual emotion understanding
* 🎨 Enhanced UI (animations, waveform visualization)

---

## 👨‍💻 Author

**Harsha Vardhan Reddy**

---

## ⭐ Summary

VocalSync AI enhances traditional TTS by adding:

✔ Emotion Intelligence
✔ Context Awareness
✔ Dynamic Voice Expression

Making machine-generated speech **more human, expressive, and engaging**.
