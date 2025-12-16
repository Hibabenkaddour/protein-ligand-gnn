# Protein–Ligand Docking Prediction using Graph Neural Networks

## Project Overview
This project focuses on predicting protein–ligand docking or activity scores by combining
graph-based representations of protein structures with molecular fingerprints of ligands.
The objective is to build an efficient screening approach for protein–ligand interactions
using modern deep learning techniques.

## Methodology
Proteins are modeled as residue-level graphs constructed from three-dimensional structures.
Each amino acid is represented as a node using its Carbon Alpha (CA) atom, and edges are
defined based on spatial proximity between residues. Node features are derived from
one-hot encoding of amino acid types.

Ligands are represented using molecular fingerprints computed from SMILES strings.
Specifically, Morgan (ECFP) and MACCS fingerprints are used to encode chemical substructures
into fixed-size numeric vectors.

Protein and ligand representations are combined and used to predict docking or activity
scores.


## Repository Structure

```text
protein-ligand-gnn/
├── data/           # Protein PDB files and ligand data
│   ├── proteins/
│   └── ligands/
├── protein/        # Protein parsing and feature extraction
├── ligand/         # Ligand fingerprint computation
├── graphs/         # Graph construction utilities
├── models/         # GNN and prediction models
├── notebooks/      # Experiments and visualizations
├── utils/          # Helper functions
├── requirements.txt
├── .gitignore
└── README.md

## Dependencies
- Python 3.9+
- BioPython
- RDKit
- NumPy
- PyTorch
- PyTorch Geometric

## References
- Graph Neural Networks and Their Current Applications in Bioinformatics, Frontiers in Genetics
- ProtTrans: Toward Understanding the Language of Life, IEEE TPAMI
- Molecular Fingerprints in Cheminformatics, Frontiers in Genetics
