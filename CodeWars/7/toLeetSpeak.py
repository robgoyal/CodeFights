# Name: toLeetSpeak.py
# Author: Robin Goyal
# Last-Modified: April 19, 2018
# Purpose: Convert a string to Leetspeak


def to_leet_speak(string):
    """
    (str) -> str

    Convert a regular english sentence consisting of uppercase
    characters and spaces to Leetspeak.

    Examples:
    >>> to_leet_speak("LEET")
    "1337"
    >>> to_leet_speak("HELLO WORLD")
    "#3110 W0R1D"
    """

    leet_alphabet = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F',
                     'G': '6', 'H': '#', 'I': '!', 'J': 'J', 'K': 'K', 'L': '1',
                     'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R',
                     'S': '$', 'T': '7', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
                     'Y': 'Y', 'Z': '2', ' ': ' '}

    return "".join([leet_alphabet[letter] for letter in str])
