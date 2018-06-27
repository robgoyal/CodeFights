# Name: alternatingSplit.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Encrypt and decrypt using an alternating split algorithm
#          Alternating split


def decrypt(encrypted_text, n):
    """decrypt

    Decrypt text using alternating split n times.

    Examples:
    >>> decrypt("iornyo abgl", 2)
    "robin goyal"
    """

    if not encrypted_text:
        return encrypted_text

    half = len(encrypted_text) // 2
    l = list(encrypted_text)

    for i in range(n):
        msg = "".join(l)
        for i in range(half + len(encrypted_text) % 2):
            l[2 * i] = msg[half + i]

        for i in range(half):
            l[2 * i + 1] = msg[i]

    return "".join(l)


def encrypt(text, n):
    """encrypt

    Encrypt text using alternating split n times.

    Algorithm: take every 2nd char from the string,
        then the other chars, that are not every 2nd
        char, and concat them as new String.

    Examples:
    >>> encrypt("robin goyal", 2)
    iornyo abgl
    """

    for i in range(n):
        text = text[1::2] + text[0::2]

    return text
