import requests
import pyttsx3
import json

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

url = "x"
r = requests.get(url)
wdic = json.loads(r.text)
speak(wdic["current"]["temp_c"])


