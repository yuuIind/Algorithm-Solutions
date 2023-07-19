def to_rna(dna_strand):
    complements = str.maketrans("ACGT", "UGCA")
    return dna_strand.translate(complements)
