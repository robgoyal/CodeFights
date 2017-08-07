# Name: lateRide.py
# Author: Robin Goyal
# Last-Modified: June 14, 2017
# Purpose: Return sum of individual digits of n minutes 
#          taken places after 00:00
#          Example: n = 808 -> 13:28 -> 1 + 3 + 2 + 8 = 14

def lateRide(n):

    # Split hours and minutes into individual digits
    hours = [int(i) for i in str(n / 60)]
    minutes = [int(i) for i in str(n % 60)]
    
    # Return sum of individual digits
    return sum(hours) + sum(minutes)