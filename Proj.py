import random
import string
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
from AppOpener import run
import subprocess
import pyautogui
import time

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
contact1="+917900464619"
contact2="+917535985236"

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  listner=sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    talk("Listening")
    listner.pause_threshold=1
    voice=listner.listen(source)
  try:
    print("Recognizing...")
    command=listner.recognize_google(voice,language='en-in')
    command=command.lower()
    if("alexa" in command):
      command=command.replace("alexa","")
      print(command)
  except Exception as e:
    print("Say that again please...")
    talk("Say that again please")
    return "None"
  return command

def sendWhatsappMessage(phone_number, message):
  currenthour = datetime.datetime.now().hour
  currentminute = datetime.datetime.now().minute
  pywhatkit.sendwhatmsg(phone_number, message, currenthour, currentminute+2,20,True,5)

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

def openWhatsapp():
  run('whatsapp')

def openChrome():
  os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

def openMsWord():
  subprocess.call("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")

def openMsExcel():
  subprocess.call("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")

def openMsPowerPoint():
  subprocess.call("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")

def randomFileName():
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))+'.png'

def take_screenshot():
  a=randomFileName()
  pyautogui.screenshot(a)

def closeCurrentWindow():
  pyautogui.hotkey('ctrl', 'w')

def closeCurrentApp():
  pyautogui.hotkey('alt', 'f4')

def switchApp():
  pyautogui.hotkey('alt', 'tab')

def openWinExplorer():
  pyautogui.hotkey('win', 'e')

def openRun():
  pyautogui.hotkey('win', 'r')

def writeText(text):
  time.sleep(5)
  pyautogui.typewrite(text)

def shutdown():
  os.system("shutdown -s -t 1")

def restart():
  os.system("restart -r -t 1")

def sleep():
  os.system("sleep -s -t 1")

def lock():
  pyautogui.hotkey('win', 'l')

def currentHour():
  return datetime.datetime.now().hour

def greetUser():
  if(currentHour()>=0 and currentHour()<12):
    talk("Good Morning")
  elif(currentHour()>=12 and currentHour()<16):
    talk("Good Afternoon")
  else:
    talk("Good Evening")

def run_alexa():
  command=take_command()
  print(command)

  if("play" in command):
    song=command.replace("play","")
    talk("playing"+song)
    pywhatkit.playonyt(song)
  
  elif("hello" in command or "hi" in command or "hey there" in command):
    talk("Hello, I am Alexa")
    talk("What can I do for you?")

  elif("how are you" in command):
    talk("I am fine, Thank you")

  elif("time" in command):
    time=datetime.datetime.now().strftime('%I %M %p')
    talk("Current time is"+time)
  
  elif("what is" in command or "who is" in command):
    person=command.replace("who the heck is","")
    info=wikipedia.summary(person)
    print(twoParagraphs(info))
    talk(twoParagraphs(info))
  
  elif("Close Current Window" in command or "close current tab" in command):
    talk("closing current window")
    closeCurrentWindow()
    
  elif("run command" in command):
    talk("opening run")
    openRun()

  elif("windows explorer" in command):
    talk("opening windows explorer")
    openWinExplorer()

  elif("exit current" in command):
    talk("closing current window")
    closeCurrentApp()

  elif("switch current" in command):
    talk("switching")
    switchApp()

  elif("write text" in command):
    talk("what do you want to write")
    text=take_command()
    writeText(text)
  
  elif("shutdown system" in command):
    talk("shutting down")
    shutdown()

  elif("restart system" in command):
    talk("restarting")
    restart()

  elif("sleep system" in command):
    talk("sleeping")
    sleep()

  elif("lock system" in command):
    talk("locking")
    lock()

  elif("date" in command):
    talk("Sorry I have a headache")
  
  elif("are you single" in command):
    talk("I am in a relationship with my wifi")
  
  elif("joke" in command):
    talk(pyjokes.get_joke())
  
  elif("microsoft word" in command):
    talk("opeining microsoft word")
    openMsWord()

  elif("open whatsapp" in command):
    talk("opening whatsapp")
    openWhatsapp()

  elif("microsoft power point" in command):
    talk("opening microsoft power point")
    openMsPowerPoint()

  elif("microsoft excel" in command):
    talk("opening microsoft excel")
    openMsExcel()

  elif("screenshot" in command):
    talk("taking screenshot")
    time.sleep(2)
    take_screenshot()

  elif("wordpad" in command):
    talk("Opening wordpad")
    openWordpad()

  elif("paint" in command):
    talk("Opening Paint")
    openPaint()

  elif("chrome" in command):
    openChrome()

  elif("calculator" in command):
    talk("Opening calculator")
    openCalculator()

  elif("close it now" in command):
    exit()

  elif("notepad" in command):
    talk("Opening Notepad")
    openNotepad()

  elif("whatsapp message" in command):
    talk("Who do you want to send a message")
    contact=take_command()
    
    if("my idea" in contact):
      talk("What message do you want to send")
      message=take_command()
      sendWhatsappMessage(contact1,message)
    
    elif("my airtel" in contact):
      talk("What message do you want to send")
      message=take_command()
      sendWhatsappMessage(contact2,message)
    
    else:
      talk("Contact not recognised")
  
  else:
    talk("please say the command again")


greetUser()
while(True):
  run_alexa()