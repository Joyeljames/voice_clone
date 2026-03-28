# 🎙️ AI Voice Studio

A modern AI-powered web application that converts **Text → Speech** and **Speech → Text** using Machine Learning models.

---

## 🚀 Features

### 🔊 Text to Speech (TTS)

* Convert text into natural-sounding voice
* Play audio instantly in browser
* Download generated audio file

### 🎤 Speech to Text (STT)

* Upload audio file (WAV/MP3)
* Convert speech into text using AI

### 🎨 Modern UI

* Clean and responsive interface
* Glassmorphism design
* Smooth user experience

---

## 🧠 Tech Stack

### Backend

* Python
* FastAPI
* Coqui TTS (for Text-to-Speech)
* Hugging Face Transformers (for Speech-to-Text)

### Frontend

* HTML
* CSS (Modern UI with gradients)
* JavaScript (Fetch API)

---

## 🏗️ Project Structure

```
voice_AI_web_application/
│
├── backend/
│   ├── main.py        # FastAPI server
│   ├── tts.py         # Text → Speech logic
│   ├── stt.py         # Speech → Text logic
│
├── frontend/
│   ├── index.html     # UI layout
│   ├── style.css      # Styling
│   ├── script.js      # API calls
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/voice-ai-app.git
cd voice-ai-app
```

### 2️⃣ Create Environment

```bash
conda create -n voice python=3.10
conda activate voice
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
cd backend
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 📸 Demo

* Enter text → generate voice
* Upload audio → get text output
* Play & download audio instantly

---

## 🧩 Architecture

```
Frontend (HTML/CSS/JS)
        ↓
FastAPI Backend
        ↓
AI Models
 ├── Coqui TTS (Text → Speech)
 └── Wav2Vec2 (Speech → Text)
```

---

## 💡 Design Decisions

* Used **FastAPI** for fast and async backend
* Chose **Coqui TTS** for stable and high-quality voice generation
* Used **Wav2Vec2** for reliable speech recognition
* Simple frontend for quick interaction and testing

---

## 🚀 Future Improvements

* 🎤 Real-time microphone recording
* 🧬 Voice cloning (custom voice generation)
* 🌐 Deploy on cloud (Render / Vercel)
* 🎨 Advanced UI (React / animations)

---

## 📌 Author

**Joyel James**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
