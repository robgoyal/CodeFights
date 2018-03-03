# Name: catYearsDogYears.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement the Cat years, Dog years challenge


def human_years_cat_years_dog_years(human_years):
    """
    (int) -> list: int

    Return the equivalent of cat years and dog years
    given the number of human years.

    Examples:
    >>> human_years_cat_years_dog_years(1)
    [1, 15, 15]
    >>> human_years_cat_years_dog_years(2)
    [2, 24, 24]
    >>> human_years_cat_years_dog_years(10)
    [10, 56, 64]
    """

    common_years = 15 * min(1, human_years) + 9 * min(1, human_years - 1)

    cat_years = common_years + 4 * max(human_years - 2, 0)
    dog_years = common_years + 5 * max(human_years - 2, 0)

    return [human_years, cat_years, dog_years]
