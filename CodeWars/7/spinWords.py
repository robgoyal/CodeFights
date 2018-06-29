# Name: spinWords.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return a string with all words with five or more letters reversed


def spin_words(sentence):
    """spin_words(sentence)

    (str) -> str

    Return a string with all words with five or more letters
    in sentence reversed.

    Examples:
    >>> spin_words("This string is not great")
    This gnirts is not taerg
    """

    return " ".join([word[::-1] if len(word) >= 5 else word
                     for word in sentence.split()])
