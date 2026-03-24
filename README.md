# 🎙️ VocalSync AI & 🎬 Pitch Visualizer

## 📌 Project Overview

**VocalSync AI** is a dual-purpose **Generative AI suite** designed to enhance professional communication through voice and visual storytelling.

It consists of two intelligent systems:

### 1️⃣ 🎙️ The Empathy Engine (TTS)

A context-aware Text-to-Speech system that converts plain text into expressive speech by dynamically modulating voice parameters based on detected emotions.

### 2️⃣ 🎬 The Pitch Visualizer (Storyboard Generator)

An AI-powered storytelling engine that transforms narratives into structured, cinematic storyboards using intelligent prompt engineering and image generation.

---

## 🚀 Key Features

### 🎙️ Challenge 1: The Empathy Engine

* 🧠 **Context-Aware Emotion Detection**
  Uses transformer-based models (`distilroberta-base`) to classify text into 7 nuanced emotions.

* 🚫 **Smart Negation Handling**
  Prevents incorrect emotion detection in phrases like *"I am not angry"*.

* 🔊 **Dynamic Vocal Modulation**
  Adjusts:

  * Speech Rate
  * Pitch
  * Volume

* 📊 **Smooth Intensity Scaling**
  Uses square-root scaling for natural emotional transitions.

---

### 🎬 Challenge 2: The Pitch Visualizer

* ✂️ **Narrative Segmentation**
  Splits input text (3–5 sentences) into meaningful scenes.

* 🧠 **Intelligent Prompt Engineering**
  Enhances raw text into cinematic prompts with:

  * Lighting
  * Style
  * Composition
  * 8K descriptors

* 🎨 **AI Image Generation**
  Integrated with **Pollinations (Flux / Stable Diffusion)** for high-quality visuals.

* 🖼 **Storyboard Rendering**
  Displays a structured, caption-based visual sequence in a modern UI.

---

## 🛠 Tech Stack

| Category       | Technology                                |
| -------------- | ----------------------------------------- |
| **Language**   | Python 3.10+                              |
| **Backend**    | FastAPI                                   |
| **NLP/ML**     | HuggingFace Transformers (PyTorch)        |
| **TTS Engine** | pyttsx3 (Offline)                         |
| **Image Gen**  | Pollinations AI (Flux / Stable Diffusion) |
| **Frontend**   | HTML5, CSS3 (Glassmorphism), Jinja2       |

---

## 📂 Project Structure

```
project/
│── main.py            # FastAPI router & server logic
│── engine.py          # Emotion detection + TTS modulation
│── visualizer.py      # Scene segmentation + prompt engineering
│── templates/
│     └── index.html   # Unified UI
│── requirements.txt
└── output.mp3         # Generated audio cache
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2️⃣ Environment Setup

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
uvicorn main:app --reload
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:8000
```

---

## 🧠 Methodology & Design Choices

### 🎨 Intelligent Prompt Engineering (Challenge 2)

To avoid weak image outputs, a **Contextual Enhancement Wrapper** is implemented.

**Example:**

* **Input:**
  `"The team worked through the night."`

* **Engineered Prompt:**
  `"Masterpiece cinematic digital art of a team working through the night, 8k resolution, professional studio lighting, highly detailed, dramatic composition."`

✅ This ensures:

* Better visual quality
* Consistent artistic style
* Rich storytelling output

---

### 🔊 Emotion-to-Voice Mapping (Challenge 1)

| Emotion | Rate        | Volume | Pitch        |
| ------- | ----------- | ------ | ------------ |
| Joy     | 1.2× Faster | High   | High         |
| Sadness | 0.7× Slower | Low    | Low          |
| Anger   | 1.3× Faster | Max    | Medium/Harsh |
| Neutral | 1.0× Base   | Medium | Steady       |

---

## 🔮 Bonus Objectives Achieved

* ✅ **Dynamic UI** – Real-time generation in a single dashboard
* ✅ **Visual Consistency** – Unified cinematic style across all images
* ✅ **Negation Awareness** – Handles complex emotional phrasing
* ✅ **Full AI Integration** – Real-time image + speech generation

---

## 📌 Example Workflow

**Input:**

```
"We worked all night to finish the project, and finally succeeded."
```

**Output:**

* 🎙 Emotion-driven speech (motivational tone)
* 🎬 3–4 scene storyboard
* 🎨 Cinematic AI-generated visuals

---

## ⚠️ Limitations

* pyttsx3 has limited pitch control (OS dependent)
* Image consistency across scenes may vary slightly
* No advanced speaker identity modeling

---

## 🔮 Future Improvements

* 🔊 Integrate ElevenLabs / Google TTS
* 🎥 Add video generation from storyboard
* ⚡ Real-time streaming audio + visuals
* 🧠 Improved contextual reasoning for prompts

---

## 👨‍💻 Author

**Harsha Vardhan Reddy**
Computer Science Undergraduate | IIIT Sri City

---

## ⭐ Final Summary

VocalSync AI combines:

✔ Emotionally Intelligent Speech
✔ AI-Powered Storytelling
✔ Advanced Prompt Engineering

