# 🤖 Jarvis - Voice Activated Virtual Assistant

## 📌 Overview

Jarvis is a Python-based voice-activated virtual assistant that performs everyday tasks through natural voice commands. It integrates speech recognition, text-to-speech, and AI capabilities to provide a seamless hands-free user experience.

The assistant can open websites, play music, fetch live news, and answer queries using the OpenAI API, making it similar to modern assistants like Alexa or Google Assistant.

---

## ✨ Features

* 🎤 **Voice Recognition** – Detects and processes user commands
* 🔊 **Text-to-Speech** – Responds using voice output (gTTS & pyttsx3)
* 🌐 **Web Automation** – Opens websites like Google, YouTube, Facebook, LinkedIn
* 🎵 **Music Playback** – Plays songs via predefined links
* 📰 **News Fetching** – Retrieves latest headlines using NewsAPI
* 🤖 **AI Integration** – Handles intelligent queries using OpenAI
* 🧠 **Wake Word Detection** – Activates on the keyword *"Jarvis"*

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* gTTS (Google Text-to-Speech)
* Pygame
* Requests
* OpenAI API
* Webbrowser

---

## 📂 Project Structure

```
jarvis/
│── main.py            # Main assistant logic
│── musicLibrary.py   # Music links dictionary
│── client.py         # OpenAI API test file
│── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis.git
cd jarvis
```

### 2️⃣ Install Dependencies

```bash
pip install speechrecognition pyttsx3 gtts pygame requests openai
```

### 3️⃣ Set Environment Variables (IMPORTANT)

Replace API keys with environment variables:

```bash
export OPENAI_API_KEY=your_openai_key
export NEWS_API_KEY=your_newsapi_key
```

---

## ▶️ How to Run

```bash
python main.py
```

* Say **"Jarvis"** to activate
* Then give commands like:

  * "Open Google"
  * "Play skyfall"
  * "Tell me the news"
  * "What is AI?"

---

## 🧠 How It Works

1. Initializes the assistant
2. Listens continuously for the wake word **"Jarvis"**
3. Captures user command via microphone
4. Processes command:

   * Predefined tasks (web, music, news)
   * AI queries via OpenAI
5. Responds using voice output

---

## 🔒 Security Note

⚠️ Do NOT upload your API keys directly to GitHub.
Always use environment variables to keep them secure.

---

## 🚀 Future Improvements

* GUI-based interface
* Offline voice recognition
* Smart home integration
* Context memory for conversations
* Mobile app version

---

## 👨‍💻 Author

**[Your Name]**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
