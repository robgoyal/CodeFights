# Name: writeNumberExpandedForm.py
# Author: Robin Goyal
# Last-Modified: March 6, 2018
# Purpose: Implement solution for Write Number in Expanded Form


def expanded_form(num):
    """
    (int) -> str

    Return a string including the expanded form of num.
    The expanded form includes the summation of its individual
    values at each placeholder.

    Examples:
    >>> expanded_form(123)
    "100 + 20 + 3"
    >>> expanded_form(7030)
    "7000 + 30"
    >>> expanded_form(57)
    "50 + 7"
    """

    placeholder_values = []
    for i, val in enumerate(str(num)):
        if int(val) != 0:
            placeholder_values.append(str(int(val) * 10 ** (len(str(num)) - i - 1)))

    return " + ".join(placeholder_values)
