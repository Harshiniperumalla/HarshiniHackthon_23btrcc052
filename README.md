# AI-Powered Voice Assistant

A Python-based voice assistant that uses local speech recognition (STT), text-to-speech (TTS), and the Google Gemini API to act as a truly conversational AI. It can also control macOS applications and send messages via WhatsApp Web.

## Prerequisites (macOS)
Since this script requires audio input, you need to install system-level audio dependencies before installing the Python packages.

1. **Install PortAudio** (Required for PyAudio to work):
   ```bash
   brew install portaudio
   ```
2. **Install Python Requirements**:
   Navigate to this directory in your terminal. You should set up a virtual environment to manage dependencies securely without interfering with macOS system packages:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
## Setup & Configuration

1. **AI Brain Setup**:
   Open `main.py` and replace `YOUR_GEMINI_API_KEY_HERE` with your actual Google Gemini API Key. You can get one for free at Google AI Studio (https://aistudio.google.com/).

2. **WhatsApp Web Setup**:
   To send WhatsApp messages, ensure you are already logged into [WhatsApp Web](https://web.whatsapp.com/) in your default browser.
   To test it, open `main.py`, find `target_number = "+0000000000"`, and replace it with your own phone number (with the country code, e.g., `+1234567890`).

## How to Run

Make sure your virtual environment is activated before running the assistant:
```bash
```
## Supported Voice Commands
- **"Open [App Name]"**: Opens a macOS application (e.g., "Open Safari", "Open Terminal", "Open Spotify").
- **"Send WhatsApp message"**: Initiates the WhatsApp web automation flow. It asks you for the message and then automates the browser.
- **"What time is it"**: Tells you the current time.
- **"Exit" / "Stop" / "Goodbye"**: Closes the assistant.
- **Anything else**: Falls back to the Google Gemini AI. The assistant will process your natural language query and respond conversationally!
