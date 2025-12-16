from protein.pdb_parser import extract_protein_from_pdb
from protein.onehot import one_hot_encode_sequence

pdb_path = "data/proteins/8HBK.pdb"
protein = extract_protein_from_pdb(pdb_path)

chain_A = protein["A"]

sequence = chain_A["sequence"]
one_hot = one_hot_encode_sequence(sequence)

print("Sequence length:", len(sequence))
print("One-hot shape:", one_hot.shape)
print("First residue:", sequence[0])
print("First one-hot vector:", one_hot[0])
