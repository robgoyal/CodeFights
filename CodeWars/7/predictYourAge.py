# Name: predictYourAge.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Implement the solution to Predict Your Age


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    """predict_age

    Predict your age using the following formula:
    - Take list of ages where each great-grandparent died
    - Multiply each number by itself
    - Add theem all together
    - Take the square root of the result
    - Divide by two

    Examples:
    >>> predict_age(65, 60, 75, 55, 60, 63, 64, 45)
    86
    """

    ages = list(locals().values())
    return math.sqrt(sum(age * age for age in ages)) // 2
