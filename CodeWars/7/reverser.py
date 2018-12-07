from math import floor, log, pow


def reverse(n):
    """reverse

    int -> int

    Returns n with all digits reversed. Assume positive n.
    Assumptions: n is positive

    >>> reverse(123)
    321
    >>> reverse(5010)
    105
    """

    digits = floor(log(n, 10)) + 1
    if digits == 1:
        return n

    return (n % 10) * int(pow(10, digits - 1)) + reverse(n // 10)
