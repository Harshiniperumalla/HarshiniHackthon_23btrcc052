import speech_recognition as sr

import pywhatkit
import os
import subprocess
import datetime
import google.generativeai as genai
# ----------------- CONFIGURATION -----------------
# 1. Provide your Google Gemini API key to make it "work like an AI"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)
# Using Gemini 1.5 Flash for fast conversational responses
model = genai.GenerativeModel('gemini-1.5-flash')
def speak(text):
    """Converts Text to Speech using macOS native 'say'"""
    print(f"\n[Assistant]: {text}\n")
    subprocess.call(["say", text])
def listen():
    """Listens to microphone input and converts to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[System]: Listening... (Speak now)")
        # Adjust for background noise for a second
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("[System]: Processing audio...")
            
            # Use Google's free web speech API for recognition
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"[User]: {query}")
            return query.lower()
        
        except sr.WaitTimeoutError:
            return "none"
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return "none"
        except sr.RequestError:
            speak("Network error. Please check your internet connection to use speech recognition.")
            return "none"
def generate_ai_response(prompt):
    """Gets conversational response from an AI Model"""
    try:
        response = model.generate_content(
            f"You are a helpful and concise voice assistant. Keep your response relatively short so it can be spoken out loud easily. User says: {prompt}"
        )
        return response.text.replace("*", "").strip() # Clean up markdown
    except Exception as e:
        return ("Sorry, I couldn't reach my AI brain. "
                "Make sure you replaced YOUR_GEMINI_API_KEY_HERE with a real key.")
def open_application(app_name):
    """Opens a macOS application using system commands"""
    try:
        # 'open -a <AppName>' works natively on macOS
        print(f"[System]: Attempting to open application '{app_name}'...")
        subprocess.call(["open", "-a", app_name])
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"I encountered an error trying to open {app_name}.")
def send_whatsapp_message():
    """Prompts for details and sends a WhatsApp message via pywhatkit"""
    speak("Who would you like to message? Please tell me their number with the country code, or configure it in my code.")
    # For safety in voice assistants, we hardcode the target or type it, as dictating complex numbers is prone to errors.
    
    # ⚠️ EDIT THIS TO A REAL NUMBER e.g., "+1234567890"
    target_number = "+0000000000" 
    
    speak("What should the message say?")
    message = listen()
    
    if message != "none":
        speak(f"Preparing to send message to configured number. I will open WhatsApp Web now. Don't touch your mouse or keyboard.")
        try:
            # Opens browser, types message, hits enter
            # You must be logged into WhatsApp Web in your default browser.
            pywhatkit.sendwhatmsg_instantly(target_number, message, wait_time=15, tab_close=True, close_time=3)
            speak("Message queued successfully.")
        except Exception as e:
            speak("Failed to deliver the message through WhatsApp Web.")
def main():
    speak("Hello! I am your AI voice assistant. How can I help you today?")
    
    while True:
        query = listen()
        if query == "none":
            continue
        # 1. Exit Commands
        if "stop" in query or "exit" in query or "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day.")
            break
            
        # 2. Open App Command
        elif "open" in query:
            # For example: "open safari" or "open Spotify"
            app_name = query.replace("open", "").strip()
            if app_name:
                open_application(app_name)
            else:
                speak("What application would you like me to open?")
                
        # 3. WhatsApp Command
        elif "whatsapp" in query or ("send" in query and "message" in query):
            send_whatsapp_message()
                 
        # 4. Utilities
        elif "what time is it" in query or "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"The time is {current_time}")
        # 5. Fallback to AI conversational mode
        else:
            speak("Let me think about that...")
            response = generate_ai_response(query)
            
            # Print the full response but speak a truncated version if it's too long
            print(f"\n[AI Generated]: {response}\n")
            if len(response) > 300:
                speak(response[:300] + "... Check the console for the full answer.")
            else:
                speak(response)
if __name__ == "__main__":
    # Ensure dependencies are working before running the loop
    main()
