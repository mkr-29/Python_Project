import datetime

def current_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time

def current_da

print(current_time())