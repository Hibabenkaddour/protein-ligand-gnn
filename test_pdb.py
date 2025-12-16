from protein.pdb_parser import extract_protein_from_pdb

pdb_path = "data/proteins/8HBK.pdb"
protein = extract_protein_from_pdb(pdb_path)

for chain_id, data in protein.items():
    print(f"Chain {chain_id}")
    print(f"  Number of residues: {len(data['sequence'])}")
    print(f"  First 5 residues: {data['sequence'][:5]}")
    print(f"  First 5 CA coords: {data['ca_coords'][:5]}")
    print()
