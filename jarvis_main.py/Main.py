import speech_recognition as sr
import webbrowser
import pyttsx3

import musicLibrary

reconizer = sr.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open chess" in c.lower():
        webbrowser.open("https://chess.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gemini" in c.lower():
        webbrowser.open("https://gemini.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ") [1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

        pass

if __name__ == "__main__":
    speak("initializing Jarvis......")

while True :
    # Listen for wake word "Jarvis"
    # obtain audio from the microphone
    r = sr.Recognizer()

    print("recognizing....")
    try:
        with sr.Microphone() as source:
            print("Listening......")
            audio = r.listen(source)

        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
            speak("Yeah Sir")

        # listen for command
        with sr.Microphone() as source:
            print("Jarvis Active.....")
            audio = r.listen(source)        
            command = r.recognize_google(audio)

            processcommand(command)

    except Exception as e:
        print("error; {0}".format(e))


    



