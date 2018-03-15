# Name: complementaryDNA.py
# Author: Robin Goyal
# Last-Modified: March 15, 2018
# Purpose: Return the complement of a DNA string


def DNA_strand(dna):
    """
    (str) -> str

    Return the DNA complement of dna as a string.

    Examples:
    >>> DNA_strand("ACTGTAC")
    "TGACATG"
    """

    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = [complements[acid] for acid in dna]

    return "".join(complement)
