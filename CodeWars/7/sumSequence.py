def sequence_sum(begin_number, end_number, step):
    """sequence_sum

    int, int, int -> int

    Return the sum of the sequence starting from begin_number
    until end_number.

    >>> sequence_sum(2, 2, 1)
    2
    >>> sequence_sum(3, 9, 2)
    24
    """

    if begin_number > end_number:
        return 0

    return begin_number + sequence_sum(begin_number + step, end_number, step)
