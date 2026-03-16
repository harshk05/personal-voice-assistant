# personal-voice-assistant project

A cross-platform, voice-controlled Python assistant that listens to spoken commands, executes actions like web search, app launching, music playback, time/IP queries, and responds via text-to-speech, with improved error handling and dynamic system-aware paths.

### What is the project?

This project is a **voice-controlled personal assistant in Python** that listens to your speech, understands simple commands, and performs actions like opening websites, playing music, telling the time, and fetching information, while replying back using text-to-speech.

### How is it made?

- Built with Python using speech recognition (to convert your voice to text) and a text-to-speech engine (to speak responses back).
- Uses a continuous loop that:
  - Listens via the microphone,
  - Converts spoken audio into text,
  - Matches the text against commands (like “open YouTube”, “play music”, “what’s the time”),
  - Executes system or web actions (open browser/app, get time/IP, query Wikipedia),
  - Handles common errors more safely (missing mic, network issues, missing files, invalid paths).
- Includes improvements over a basic version: dynamic user paths instead of hardcoded ones, ambient-noise adjustment, better exception handling, and more portable app-launch logic.

### How to use the project?

You can adapt this for your README like this:

1. **Install dependencies**  
   - Install Python 3.  
   - Install required packages (example):  
     ```bash
     pip install speechrecognition pyttsx3 wikipedia requests pyaudio
     ```
     (Plus any extra libraries you added, like vosk/whisper if you integrated offline recognition.)

2. **Set up your environment**  
   - Make sure your microphone and speakers are working and set as default on your system.  
   - Optionally adjust any paths (e.g., music folder, specific apps) in the script if you want to customize behavior.

3. **Run the assistant**  
   - From the project directory:  
     ```bash
     python assistant_enhanced.py
     ```  
   - Wait for the greeting, then speak commands such as:
     - “open youtube”
     - “open google”
     - “play music”
     - “what is the time”
     - “search wikipedia for Python”
     - “what is my IP address”
   - Say “quit”, “exit”, or “close” to stop the assistant.

If you tell me which features you finally kept in `assistant_enhanced.py` (e.g., Vosk/Whisper/offline mode or only Google API), I can rewrite this into a fully polished README section with exact commands.
