def is_isogram(string):
    """is_isogram

    str -> bool

    Produce true if the string is an isogram, false otherwise.

    >>> is_isogram("")
    True
    >>> is_isogram("lumberjacks")
    True
    >>> is_isogram("isograms")
    False
    """

    freq_arr = [False] * 26

    for char in string:
        if char.isalpha():
            index = ord(char.lower()) - 97
            if freq_arr[index]:
                return False
            freq_arr[index] = not freq_arr[index]

    return True