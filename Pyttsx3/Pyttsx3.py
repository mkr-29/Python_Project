import pyttsx3

"""pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3."""

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

say("Hello World")