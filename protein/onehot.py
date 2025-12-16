import numpy as np

# 20 standard amino acids (3-letter codes)
AMINO_ACIDS = [
    "ALA", "ARG", "ASN", "ASP", "CYS",
    "GLN", "GLU", "GLY", "HIS", "ILE",
    "LEU", "LYS", "MET", "PHE", "PRO",
    "SER", "THR", "TRP", "TYR", "VAL"
]

AA_TO_INDEX = {aa: i for i, aa in enumerate(AMINO_ACIDS)}

UNKNOWN_INDEX = len(AMINO_ACIDS)  # index 20
def one_hot_encode_sequence(sequence):
    """
    One-hot encode a protein sequence.

    Parameters
    ----------
    sequence : list of str
        Amino acid residue names (e.g. ["ALA", "GLY", "VAL"])

    Returns
    -------
    np.ndarray
        Array of shape (N, 21) where N is the number of residues.
    """

    num_residues = len(sequence)
    one_hot = np.zeros((num_residues, len(AMINO_ACIDS) + 1))

    for i, aa in enumerate(sequence):
        if aa in AA_TO_INDEX:
            one_hot[i, AA_TO_INDEX[aa]] = 1.0
        else:
            # Unknown or non-standard amino acid
            one_hot[i, UNKNOWN_INDEX] = 1.0

    return one_hot
