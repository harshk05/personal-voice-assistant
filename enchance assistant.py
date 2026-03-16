import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import platform
import shutil
from requests import get, RequestException

# Initialize Text-to-Speech Engine
# Removed 'sapi5' specific init to allow auto-detection on non-Windows platforms
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Safe voice selection: try to find a female voice or default to the first one available
    voice_set = False
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            voice_set = True
            break
    if not voice_set and voices:
        engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(f"Error initializing TTS engine: {e}")
    sys.exit(1)

def speak(audio):
    """Outputs audio via TTS engine."""
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception:
        print(f"Assistant: {audio}") # Fallback to text if audio fails

def wishMe():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How may I help you?")

def takeCommand():
    """Listens to microphone input and returns string query."""
    r = sr.Recognizer()
    
    # FIX: Removed hardcoded device_index=1. Uses default system microphone.
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1) # FIX: Calibrates for background noise
            audio = r.listen(source, timeout=5, phrase_time_limit=10) # FIX: Added timeouts
    except OSError:
        print("Microphone not found or inaccessible.")
        return "None"
    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def open_application(app_name, specific_path=None):
    """Cross-platform application launcher helper."""
    try:
        if sys.platform == 'win32':
            if specific_path and os.path.exists(specific_path):
                os.startfile(specific_path)
            else:
                # Try finding in PATH
                cmd = shutil.which(app_name)
                if cmd:
                    os.startfile(cmd)
                else:
                    speak(f"Could not find {app_name} installed.")
        elif sys.platform == 'darwin': # macOS
            os.system(f"open -a {app_name}")
        else: # Linux
            os.system(f"{app_name}")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue

        # --- Logic for executing tasks based on query ---
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("I couldn't find a page matching that query.")
            except wikipedia.exceptions.DisambiguationError:
                speak("There are too many results for that topic. Please be more specific.")
            except Exception:
                speak("I encountered an error searching Wikipedia.")

        elif 'hello' in query:
            speak('Hello! How can I help you?')

        elif 'open youtube' in query:
            speak('Opening YouTube')
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in query:
            speak('Opening Facebook')
            webbrowser.open("https://www.facebook.com")
            
        elif 'open search' in query:
            speak('What should I search on the Internet?')
            cm = takeCommand().lower()
            if cm != "none":
                webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif 'ip address' in query:
            try:
                ip = get('https://api.ipify.org').text
                print(f"IP: {ip}")
                speak(f"Your IP Address is {ip}")
            except RequestException:
                speak("I couldn't connect to the internet to get your IP.")

        elif 'play music' in query:
            speak('Playing music')
            # FIX: Dynamic path to user's music folder
            music_dir = os.path.join(os.path.expanduser("~"), "Music")
            if os.path.exists(music_dir):
                songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
                if songs:
                    if sys.platform == 'win32':
                        os.startfile(os.path.join(music_dir, songs[0]))
                    else:
                        # Basic fallback for non-Windows
                        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
                        subprocess.call([opener, os.path.join(music_dir, songs[0])])
                else:
                    speak("No music files found in your Music folder.")
            else:
                speak("I cannot find your Music folder.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vscode' in query:
            speak('Opening VS Code')
            # Uses 'code' command which is standard if VS Code is in PATH
            open_application("code", r"C:\Users\harsh\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'open browser' in query:
            speak('Opening Browser')
            # Generic fallback to default browser if Brave path fails
            open_application("brave", r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

        elif 'quit' in query or 'exit' in query or 'close' in query:
            speak("Goodbye!")
            sys.exit()
