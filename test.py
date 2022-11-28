import datetime

def currentHour():
    return datetime.datetime.now().hour

def greetUser():
    if(currentHour()>=0 and currentHour()<12):
        talk("Good Morning")
    elif(currentHour()>=12 and currentHour()<16):
        talk("Good Afternoon")
    else:
        talk("Good Evening")

greetUser()