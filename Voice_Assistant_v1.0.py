import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Your Assistant. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:      
        #print (e)
        print("Say that again please...")
        speak("Can't recognise, Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            print("Hello, how can i help you")
            speak('Hello, how can i help you')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com") 

        elif 'open search' in query:
            speak('What should I search on Internet?')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com") 

        elif 'how are you' in query:
            print("I m fine, how can i help you")
            speak('I m fine, how can i help you')  

        elif 'ip address'in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your IP Address id {ip}")

        elif 'play music' in query:
            speak('playing music')
            music_dir = "C:\\Users\\harsh\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vscode' in query:
            speak('opening vscode')
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open browser' in query:
            speak('opening browser')
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)


        elif 'quit' in query or 'exit' in query or 'close' in query:
            speak("Thank you, Assistant is now closing")
            exit()
