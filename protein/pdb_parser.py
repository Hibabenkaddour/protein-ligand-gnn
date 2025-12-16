from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa


def extract_protein_from_pdb(pdb_path):
    """
    Extract amino acid sequences and CA coordinates for all chains in a PDB file.

    Parameters
    ----------
    pdb_path : str
        Path to the PDB file.

    Returns
    -------
    dict
        Dictionary of the form:
        {
            chain_id: {
                "sequence": [residue names],
                "ca_coords": [(x, y, z), ...]
            }
        }
    """

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_path)

    protein_data = {}

    for model in structure:
        for chain in model:
            sequence = []
            ca_coords = []

            for residue in chain:
                # Keep only amino acids
                if not is_aa(residue):
                    continue

                # Keep only residues with a CA atom
                if "CA" not in residue:
                    continue

                # Residue name (e.g. ALA, GLY)
                res_name = residue.get_resname()

                # CA coordinates
                ca_coord = residue["CA"].get_coord()

                sequence.append(res_name)
                ca_coords.append(tuple(ca_coord))

            if len(sequence) > 0:
                protein_data[chain.id] = {
                    "sequence": sequence,
                    "ca_coords": ca_coords
                }

    return protein_data
