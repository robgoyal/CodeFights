# Name: reverseParentheses.py
# Author: Robin Goyal
# Last-Modified: June 22, 2017
# Purpose: Reverse the strings in parentheses starting
#          from the innermost pair

def reverseParentheses(s):

    openingIndex = []
    chars = list(s)

    for i in range(len(chars)):

        # Store indices of opening brackets
        if chars[i] == '(':
            openingIndex.append(i)

        # Reverse subset of list in between opening and closed bracket
        elif chars[i] == ')':
            index = openingIndex.pop()
            chars[index + 1 : i] = chars[i-1 : index : -1]

    # Remove all ( ) and join list to string
    return ''.join([x for x in chars if (x != '(' and x != ')')])