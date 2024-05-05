# Zero Knowledge Proof (ZKP) for Matrix Multiplication

This repository contains a Python implementation of a Zero Knowledge Proof (ZKP) protocol for proving knowledge of matrix multiplication using cryptographic commitments.

## Overview

The ZKP protocol implemented here demonstrates how a prover can convince a verifier that they know the product of two matrices (A and B) without revealing the matrices themselves. This is achieved through the use of commitment schemes and challenge-response interactions.

## Dependencies

- Python 3.x
- `petlib` library (for cryptographic operations)

1. Install `petlib` using pip:

    pip install petlib

------------------------------
2. Implementation Details

   - zkp_matrix_multiplication.py: Contains the implementation of the ZKP protocol for matrix multiplication.
   - generate_random_matrix(rows, cols): Generates a random matrix.
   - commit_matrix(matrix): Computes Pedersen commitments for a given matrix.
   - prove_knowledge_of_product(A, B, A_commitment, B_commitment): Prover's function to prove knowledge of matrix product 𝐴 × 𝐵 A × B.
   - verify_proof(A_commitment, B_commitment, r_C, challenge): Verifier's function to verify the prover's response.

---------------------------------------

How to Run :

Step 1: Clone the Repository
Clone the GitHub repository to your local machine using the following command:

git clone https://github.com/your-username/zkp-matrix-multiplication.git

Replace your-username with your actual GitHub username.

Step 2: Navigate to the Repository Directory

Navigate to the cloned repository directory using the following command:

	cd zkp-matrix-multiplication

Step 3: Run the Python Script

Run the Python script using the following command:


	python zkp_matrix_multiplication.py

Step 4: Review the Output

  The script will generate random matrices \( A \) and \( B \), perform matrix multiplication \( A times B \), and output the result along 
  with the verification message.

## Expected Output

The output of the script should include the following:

- Proof verification message indicating whether the prover's knowledge of the matrix product was successfully verified.
- Matrices \( A \) and \( B \).
- Matrix product \( A \times B \).

Example output:

Proof verified: Prover knows the matrix product A*B
Matrix A:
9 8
8 2
9 9
Matrix B:
0 6 6 4
4 3 4 9
Matrix Product (A*B):
32 78 86 108
8 54 56 50
36 81 90 117
