def is_leap_year(year):
    """
    int -> bool

    Return true if the given year is a
    leap year, false otherwise.

    >>> is_leap_year(2016)
    True
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    """

    return (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0))
