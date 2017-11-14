# Name: timeConversion.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Convert 12-Hour time format to 24-Hour time

def timeConversion(s):

    # Time information
    time_of_day = s[len(s)-2:]
    time_str = s[0:len(s)-2]

    # Hour of time input
    hour = int(time_str[0:2])

    # Between 1 PM and 12 AM
    if time_of_day == 'PM' and hour != 12:
        return str(hour + 12) + time_str[2:]

    # Between 12 and 1 AM
    elif time_of_day == 'AM' and hour == 12:
        return '00' + time_str[2:]

    else:
        return time_str