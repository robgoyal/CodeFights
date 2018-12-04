def hey(phrase):
    """
    str -> str

    Return responses depending on what is said to Bob.

    >>> hey("Tom-ay-to, tom-aaaah-to.")
    "Whatever."
    >>> hey("WATCH OUT!")
    "Whoa, chill out!"
    >>> hey("You are, what, like 15?")
    "Sure."
    >>> hey("WHAT THE HELL WERE YOU THINKING?")
    "Calm down, I know what I'm doing!"
    >>> hey("")
    "Fine. Be that way!"
    """

    phrase = phrase.strip()
    answer = ""

    if phrase.endswith("?") and phrase.isupper():
        answer = "Calm down, I know what I'm doing!"
    elif phrase.endswith("?"):
        answer = "Sure."
    elif phrase.isupper():
        answer = "Whoa, chill out!"
    elif not phrase:
        answer = "Fine. Be that way!"
    else:
        answer = "Whatever."

    return answer
