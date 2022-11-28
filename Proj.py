import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

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

def sendWhatsappMessage(phone_number, message):
    currenthour = datetime.datetime.now().hour
    currentminute = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(phone_number, message, currenthour, currentminute+1,20,True,5)

def twoParagraphs(text):
    return text.split(".")[0] + "." + text.split(".")[1] + "."

def openNotepad():
    os.system("notepad.exe")

def openPaint():
    os.system("mspaint.exe")

def openCalculator():
    os.system("calc.exe")

def openWordpad():
    os.system("write.exe")


















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
    print(twoParagraphs(info))
    talk(twoParagraphs(info))
  
  elif("date" in command):
    talk("Sorry I have a headache")
  
  elif("are you single" in command):
    talk("I am in a relationship with my wifi")
  
  elif("joke" in command):
    talk(pyjokes.get_joke())
  
  # elif("wordpad" in command):

  elif("wordpad" in command):
    talk("Opening wordpad")
    openWordpad()

  elif("paint" in command):
    talk("Opening Paint")
    openPaint

  elif("calculator" in command):
    talk("Opening calculator")
    openCalculator()

  elif("notepad" in command):
    talk("Opening Notepad")
    openNotepad()

  elif("whatsapp" in command):
    talk("Who do you want to send a message")
    contact=take_command()
    
    if("contact1" in contact):
      talk("What message do you want to send")
      message=take_command()
      sendWhatsappMessage(contact1,message)
    
    elif("contact2" in contact):
      talk("What message do you want to send")
      message=take_command()
      sendWhatsappMessage(contact2,message)
    
    else:
      talk("Contact not recognised")
  
  else:
    talk("please say the command again")

while(True):
  run_alexa()