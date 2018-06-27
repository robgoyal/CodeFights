# Name: nameList.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Format a string of names like 'Bart, Lisa & Maggie'


def namelist(names):
    """namelist

    Return a string formatted from a dictionary, names.

    Examples:
    >>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
    "Bart, Lisa & Maggie"
    >>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}])
    'Bart & Lisa'
    >>> namelist([{'name': 'Bart'}])
    'Bart'
    >>> namelist([])
    ''
    """

    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names[0]["name"]

    names = [name["name"] for name in names]
    return ", ".join(names[:len(names) - 1]) + " & " + names[-1]
