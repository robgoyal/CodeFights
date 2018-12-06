def to_rna(dna_strand):
    """to_rna

    str -> str

    Produce the RNA complement of the DNA strand.

    >>> to_rna("")
    ""
    >>> to_rna("ACTG")
    "UGAC"
    """

    complements = {"A": "U", "T": "A", "C": "G", "G": "C"}

    rna_strand = []
    try:
        for nucleotide in dna_strand:
            rna_strand.append(complements[nucleotide])
    except KeyError:
        raise ValueError("Invalid nucleotide in DNA strand")

    return "".join(rna_strand)