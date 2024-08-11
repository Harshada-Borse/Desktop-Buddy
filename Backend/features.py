from playsound import playsound
import eel
import os

@eel.expose
def playStartSound():
    music_dir = "assets\\start_sound.mp3"
    playsound(music_dir)
    

def openCommand(query):
    query = query.replace(AssistantName, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening" + query)
        os.system('start' + query)
    else:
        speak("Not found the app in your PC")