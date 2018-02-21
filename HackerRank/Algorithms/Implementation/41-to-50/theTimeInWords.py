# Name: theTimeInWords.py
# Author: Robin Goyal
# Last-Modified: February 21, 2018
# Purpose: Convert time to words


def timeInWords(h, m):
    '''
    (int, int) -> str

    Preconditions: 1 <= h < 12
                   0 <= m < 60

    Convert the time give hours h and minutes m into
    a string.

    Examples:
    >>> timeInWords(5, 00)
    five o' clock
    >>> timeInWords(5, 10)
    ten minutes past five
    >>> timeInWords(5, 45)
    quarter to six
    '''

    # Create an indexable array to convert numbers to words
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
             'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six',
             'twenty seven', 'twenty eight', 'twenty nine']

    # Initialize common phrases for times such as 5:00, 5:30, 5:15, 5:45, 5:01, 5:59
    common_phrases = {0: "{} o' clock".format(words[h]), 15: "quarter past {}".format(words[h]),
                      30: "half past {}".format(words[h]), 45: "quarter to {}".format(words[h + 1]),
                      1: "{} minute past {}".format(words[1], words[h]), 59: "{} minute to {}".format(words[1], words[h])}

    # Check if minutes can return a common phrase
    if m in common_phrases:
        time_str = common_phrases[m]

    # Minutes is in first half of hour
    elif m < 30:
        time_str = "{} minutes past {}".format(words[m], words[h])
    # Minutes is in second half of hour
    else:
        time_str = "{} minutes to {}".format(words[60 - m], words[h + 1])

    return time_str
