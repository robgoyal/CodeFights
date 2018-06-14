# Name: electionsWeightedAverage.py
# Author: Robin Goyal
# Last-Modified: June 13, 2018
# Purpose: Return a weighted average of election results


def predict(candidates: list, polls: list) -> dict:
    """predict

    Return a dictionary containing the weighted average
    for each candidate in candidates. The polls list
    contains a list of lists, where the first element
    in the nested list is the poll result for each candidate
    and the second element is the weight.

    Example:
    >>> candidates = ['A', 'B', 'C']
    >>> poll1 = [[20, 30, 50], 1]
    >>> poll2 = [[40, 40, 20], 0.5]
    >>> poll3 = [[50, 40, 10], 2]
    >>> polls = [poll1, poll2, poll3]
    >>> predict(candidates, polls)
    {'A': 40, 'B': 37.1, 'C': 22.9}
    """

    projection = {}

    # Calculate total weight
    weights = sum(poll[-1] for poll in polls)

    for index, candidate in enumerate(candidates):
        score = sum(res[index] * wt for res, wt in polls)

        # round1 is provided method for rounding to 1 decimal place
        projection[candidate] = round1(score / weights)

    return projection
