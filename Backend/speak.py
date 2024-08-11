import pyttsx3 # check it's documentation for more information
import speech_recognition as sr
import eel

@eel.expose
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        eel.DisplayMessage('Listening.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recongnizing.....")
        eel.DisplayMessage('Recongnizing.....')
        query = r.recognize_google(audio, language ='en-in')
        print({f"user said: {query}"})
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowInterface()
    except Exception as e:
        return ""
    
    return query.lower()

def speak(text):
    engine = pyttsx3.init('sapi5') # sapi5 <= all microsoft voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #indexing for available voices
    engine.setProperty('rate', 174) # standard rate of speak
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def allCommands():

    query = takeCommand()
    print(query)

    if "open" in query:
        print("I Run")
    else:
        print("Not Run")
