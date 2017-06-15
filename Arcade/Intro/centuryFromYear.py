# Name: centuryFromYear.py
# Author: Robin Goyal
# Last-Modified: May 15, 2017
# Purpose: Return the century from year

def centuryFromYear(year):
    if year % 100 == 0:
        return year / 100
    else:
        return year / 100 + 1