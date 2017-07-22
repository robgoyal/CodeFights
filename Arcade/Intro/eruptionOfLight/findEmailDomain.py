# Name: findEmailDomain.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: Find the email domain in a string

def findEmailDomain(address):

    # Find last occurrences of @
    index = max(loc for loc, val in enumerate(address) if val == '@')
    return address[index + 1:]