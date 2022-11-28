import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
contact1="+917900464619"
contact2="+917535985236"

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
    try:
      with sr.Microphone() as source:
        print("Listening...")
        voice=listner.listen(source)
        command=listner.recognize_google(voice)
        command-command.lower()
        if("alexa" in command):
          command=command.replace("alexa","")
          print(command)
    except:
      pass
    return command

def sendW

def run_alexa():
  command=take_command()
  print(command)
  if("play" in command):
    song=command.replace("play","")
    talk("playing"+song)
    pywhatkit.playonyt(song)
  elif("time" in command):
    time=datetime.datetime.now().strftime('%I:%M %p')
    talk("Current time is"+time)
  elif("who the heck is" in command):
    person=command.replace("who the heck is","")
    info=wikipedia.summary(person)
    print(info)
    talk(info)
  elif("date" in command):
    talk("Sorry I have a headache")
  elif("are you single" in command):
    talk("I am in a relationship with my wifi")
  elif("joke" in command):
    talk(pyjokes.get_joke())
  else:
    talk("please say the command again")

while(True):
  run_alexa()