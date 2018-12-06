def is_pangram(sentence):
    """is_pangram

    str -> bool

    Produce True if every letter of alphabet is used.

    >>> is_pangram("The quick brown fox jumps over the lazy dog.")
    True
    >>> is_pangram("Hello")
    False
    """

    alphabet_arr = [False] * 26

    for char in sentence:
        if char.isalpha():
            index = ord(char.lower()) - 97
            alphabet_arr[index] = True

    return all(alphabet_arr)