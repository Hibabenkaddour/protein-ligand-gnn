# =========================
# Test script for Step 4
# Protein + Ligand features
# =========================

from protein.pdb_parser import extract_protein_from_pdb
from protein.onehot import one_hot_encode_sequence
from ligand.fingerprints import morgan_fingerprint, maccs_fingerprint


def test_protein_processing():
    print("=== Testing protein PDB processing ===")

    pdb_path = "data/proteins/8HBK.pdb"
    protein_data = extract_protein_from_pdb(pdb_path)

    # Take chain A as example
    chain_id = "A"
    chain = protein_data[chain_id]

    sequence = chain["sequence"]
    ca_coords = chain["ca_coords"]

    one_hot = one_hot_encode_sequence(sequence)

    print(f"Chain {chain_id}")
    print(f"Number of residues: {len(sequence)}")
    print(f"One-hot shape: {one_hot.shape}")
    print(f"CA coords shape: ({len(ca_coords)}, 3)")
    print(f"First residue: {sequence[0]}")
    print(f"First CA coord: {ca_coords[0]}")
    print(f"First one-hot vector: {one_hot[0]}")
    print()


def test_ligand_processing():
    print("=== Testing ligand fingerprints ===")

    # Example ligand: Paracetamol
    smiles = "CC(=O)Nc1ccc(O)cc1"

    morgan_fp = morgan_fingerprint(smiles)
    maccs_fp = maccs_fingerprint(smiles)

    print("SMILES:", smiles)
    print("Morgan fingerprint shape:", morgan_fp.shape)
    print("MACCS fingerprint shape:", maccs_fp.shape)
    print("Morgan fingerprint (first 20 bits):", morgan_fp[:20])
    print("MACCS fingerprint (first 20 bits):", maccs_fp[:20])
    print()


if __name__ == "__main__":
    test_protein_processing()
    test_ligand_processing()
