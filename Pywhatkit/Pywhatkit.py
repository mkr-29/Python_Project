import pywhatkit
import datetime

def sendWhatsappMessage(phone_number, message):
    currenthour = datetime.datetime.now().hour
    currentminute = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(phone_number, message, currenthour, currentminute+1,20,True,5)

def sendWhatsappImage(phone_number, image_path,message):
    currenthour = datetime.datetime.now().hour
    currentminute = datetime.datetime.now().minute
    pywhatkit.sendwhats_image(phone_number, image_path, message)

def convertToImage(text):
    return pywhatkit.text_to_handwriting(text)

def convertImageToAscii(image_path):
    return pywhatkit.image_to_ascii_art(image_path)

def playOnYoutube(search_query):
    pywhatkit.playonyt(search_query)

def searchOnGoogle(search_query):
    pywhatkit.search(search_query)

def sendEmail(email_address, password, message, email_subject, email_attachment):
    pywhatkit.send_mail(email_address, password, message, email_subject, email_attachment)

sendWhatsappMessage("+917900464619", "Hello World")
sendWhatsappImage("+917900464619", "D://College//Python//Python_Project//Pywhatkit//Images//designbig.jpg","Hello World")
convertToImage("Hello World")
convertImageToAscii("D://College//Python//Python_Project//Pywhatkit//Images//designbig.jpg")
playOnYoutube("Closer")
searchOnGoogle("Adam Levine")