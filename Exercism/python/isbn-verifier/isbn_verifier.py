def verify(isbn):
    """
    str -> bool

    Verify if the string is a valid ISBN number.

    Examples:
    >>> verify("3-598-21508-8")
    True
    >>> verify("359821507X")
    True
    """

    isbn = isbn.replace("-", "")
    if not verify_format(isbn):
        return False

    isbn_sum = 0
    for digit, i in zip(isbn, range(10, 0, -1)):
        if digit == "X":
            isbn_sum += 10 * i
        else:
            isbn_sum += int(digit) * i

    return isbn_sum % 11 == 0


def verify_format(isbn):
    """
    str -> bool

    Verify if the isbn is of a valid format.

    Examples:
    >>> verify("359182356P")
    False
    >>> verify("3-598-21508-8")
    True
    >>> verify("1827P2858X")
    False
    """

    return len(isbn) == 10 and (isbn[-1] == "X" or isbn[-1].isdigit()) \
        and all(digit.isdigit() for digit in isbn[:-1])
