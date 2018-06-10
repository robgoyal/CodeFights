# Name: decodeMorse.py
# Author: Robin Goyal
# Last-Modified: June 10, 2018
# Purpose: Decode a morse code encoded string


def decodeMorse(morse_code):
    """decodeMorse

    Return a string representing the decoded
    version of morse_code. MORSE_CODE is a
    preloaded dictionary containing the mapping.

    Examples:
    >>> decodeeMorse("-- -.--  -. .- -- .  .. ...  -... --- -...")
    MY NAME IS BOB
    """

    words = morse_code.strip().split('  ')
    decoded = [[MORSE_CODE[letter] for letter in word.strip().split(' ')] for word in words
    return ' '.join(''.join(word) for word in decoded)
