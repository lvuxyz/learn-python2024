import os
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb

friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)

def speak(audio):
    print('BOT 0.1: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(current_time)

def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good morning")
    speak('can you help me?')

def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 2
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print("Vincent Vu: " + query)
    except sr.UnknownValueError:
        print("please repeat or typing the command")
        query = str(input('your order is: '))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("what should i search boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.open(url)
            speak(f'here is your {search} on google')

        if "youtube" in query:
            speak("what should i search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.open(url)
            speak(f'here is your {search} in youtube')

        elif "open video" in query:
            meme=r"C:\Users\hello1love\Videos\hahathayba.mp4"
            os.startfile(meme)

        elif "time" in query:
            time()

        elif "quit" in query:
            speak("Friday is quiting sir. goodbye boss")
            quit()