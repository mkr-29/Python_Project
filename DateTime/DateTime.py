import datetime

def current_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time

def current_date():
    current_date = datetime.datetime.now().strftime('%A %d %B %Y')
    return current_date

def current_datetime():
    current_datetime = datetime.datetime.now().strftime('%A %d %B %Y %I:%M %p')
    return current_datetime

def current_year():
    current_year = datetime.datetime.now().strftime('%Y')
    return current_year

def current_month():
    current_month = datetime.datetime.now().strftime('%B')
    return current_month

def current_day():
    current_day = datetime.datetime.now().strftime('%A')
    return current_day

def current_hour():
    current_hour = datetime.datetime.now().strftime('%I')
    return current_hour

def festival():
    current_month = datetime.datetime.now().strftime('%B')
    current_day = datetime.datetime.now().strftime('%d')
    if current_month == 'January' and current_day == '01':
        return 'Happy New Year'
    elif current_month == 'February' and current_day == '14':
        return 'Happy Valentine\'s Day'
    elif current_month == 'March' and current_day == '08':
        return 'Happy International Women\'s Day'
    elif current_month == 'March' and current_day == '17':
        return 'Happy St. Patrick\'s Day'
    elif current_month == 'April' and current_day == '01':
        return 'Happy April Fools\' Day'
    elif current_month == 'May' and current_day == '01':
        return 'Happy Labour Day'
    elif current_month == 'May' and current_day == '25':
        return 'Happy Africa Day'
    elif current_month == 'June' and current_day == '01':
        return 'Happy Children\'s Day'
    elif current_month == 'June' and current_day == '12':
        return 'Happy World Day Against Child Labour'
    elif current_month == 'July' and current_day == '01':
        return 'Happy Canada Day'
    elif current_month == 'August' and current_day == '01':
        return 'Happy Independence Day'
    elif current_month == 'August' and current_day == '15':
        return 'Happy Eid al-Adha'
    elif current_month == 'September' and current_day == '01':
        return 'Happy Eid al-Fitr'

current_time()
current_date()
current_datetime()
current_year()
current_month()
current_day()
current_hour()
festival()