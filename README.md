# Voice Interactive Chatbot (Powered by Ollama + Speech Recognition)

This project is a **voice-controlled chatbot** that enables natural spoken conversations with an AI model locally, using [Ollama](https://ollama.ai).  
It listens to your speech, converts it to text, generates a response using the **LLaMA 2** model, and speaks the response back to you using **text-to-speech**.

---

## Features

- **AI Model Integration:** Uses **LLaMA 2** via the Ollama API for intelligent text generation.  
- **Speech Recognition:** Converts spoken words to text using the **SpeechRecognition** library.  
- **Text-to-Speech:** Responds naturally with **pyttsx3**, allowing real-time conversation.  
- **Voice Filtering:** Detects and blocks inappropriate language.  
- **Voice Commands:** Say **"exit"** anytime to quit the chatbot.  
- **Customizable Voice Settings:** Choose speaking rate and voice tone.

---

## How It Works

1. The program initializes:
   - `ollama.Client()` for AI interaction.
   - `speech_recognition.Recognizer()` for listening to your microphone.
   - `pyttsx3` for converting text to speech.
2. The user speaks into the microphone.
3. Speech is transcribed to text and sent to the **LLaMA 2** model.
4. The AI generates a response, which is both printed and spoken aloud.
5. Say **"exit"** to gracefully end the conversation.

---

## Requirements

Ensure you have **Python 3.8 or later** installed.

### Install dependencies
```bash
pip install -r requirements.txt
```
---
## Author
**Kwabena Amoako**  
Embedded Systems | Hardware & Firmware | Robotics

📫 Connect on [GitHub](https://github.com/kobbieessel)  
💼 Passionate about AI, embedded systems, and automation projects.
Social:
[LinkedIn](https://www.linkedin.com/in/kwabena-e-amoako/)
---

## License

This project is licensed under the **MIT License** – feel free to use, share, and modify it.


---





