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

  Zero-Knowledge Proof Library (zkp_library.py)
This module provides functions to generate and verify zero-knowledge proofs for matrix multiplication using commitment schemes and hash functions.

generate_proof(matrix_A, matrix_B):
Generates a zero-knowledge proof for the multiplication of matrices matrix_A and matrix_B.
Returns the commitment to matrix_A and matrix_B, a challenge, and the response.
verify_proof(proof, matrix_A, matrix_B):
Verifies the zero-knowledge proof for the multiplication of matrices matrix_A and matrix_B.
Returns True if the proof is valid, False otherwise.
commit_matrix(matrix):
Computes the commitment to a given matrix.
compute_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge):
Computes the response to a challenge.
verify_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge, response):
Verifies the response to a challenge.
generate_random_matrix(rows, cols):
Generates a random matrix with the specified number of rows and columns.
Matrix Multiplication Zero-Knowledge Proof Script (zkp_matrix_multiplication.py)
This script demonstrates the usage of the zero-knowledge proof library for multiple rounds of matrix multiplication.

main():
Defines parameters for multiple rounds of matrix multiplication.
Generates random matrices for each round.
Generates a zero-knowledge proof for each pair of matrices and verifies the proof.
Prints the matrices, proof, proof generation time, proof verification time, and proof size in memory for each round.
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

Round 1:

Matrix A:
[0, 8, 1]
[6, 8, 6]

Matrix B:
[2, 2]
[7, 6]
[2, 2]

Proof: (b'\xe5\xae0%\x98\xa5\xae\x9f\x0c\x85\x80P8u\xc7\xcd^%\xe2:\x196U\x0c\xc9\xd5\xf0\x8d$t\x19\xa5', b'\xea\x03N\xe1\x87kR\x1a\x85y\x1e1\x85&*\xd1\x9a\xd2\xa4\rlK\xc4\x0e\xde\xd1\xef"\xfdM\xceS', 43586197249284657265949170653846338793401651076195342694631750620953578967201, b'G\x08G\xd8\xdeb\xe1\xdb_\xd0\xfe\x07\xd3\xd7\xc6\x1d\xb5\xd7\x06\xb3\x9d\xc7}\xe7B\xa4\xd4\x90<:\x13q')

Proof verified: True
Proof generation time: 0.000013 seconds
Proof verification time: 0.000005 seconds
Proof size in memory: 72 bytes

Round 2:

Matrix A:
[9, 4]
[4, 9]
[7, 7]

Matrix B:
[5, 8, 7]
[7, 9, 1]

Proof: (b'S\xa9\xb2LB\x8a\xf2\xaf_H\x8f\xd2\xc8\x91\xd4\xc3NOh9\xad\x83\xfe\r)\xcde\x1dZ\xab/\xa9', b'\xdc\t\xa1S\x94\xc3\xbc\xfdf \xa6\xdap\xabS\xb5\xc4\x96"\xd4M&C\xb2ZM|\xb0\x0e\xff\xd5\x8a', 103950535508311266486460580583949942186240641729988009549691784844261405574240, b'\xcc\x00\xb3%"\xccAe*(l+u\xccn\xe1+\x97\xc1X\\\xcfrwQ\xe1\'Wpq\x05\xb2')

Proof verified: True
Proof generation time: 0.000006 seconds
Proof verification time: 0.000006 seconds
Proof size in memory: 72 bytes

Round 3:

Matrix A:
[8, 4, 6, 5, 1]
[1, 0, 8, 5, 8]
[8, 1, 0, 8, 3]
[6, 6, 8, 0, 5]
[4, 3, 8, 0, 5]

Matrix B:
[6, 3, 2, 1, 5]
[9, 0, 6, 0, 0]
[6, 9, 3, 8, 6]
[2, 1, 8, 3, 3]
[9, 7, 8, 4, 0]

Proof: (b'}\x0f\xc3\xd0o\x95o\x1e$\xa8=\xf873\ta=)"\x0ch:g\xc8\xcd#\xe65o\xa3sl', b'\xc3\xc0 o\xc4\xa0\x8b\xb9\xb2\xa0\x1f\n\xefo\xa6q\x13\xb8\xce\x96\x1c\xbf-\x97Uj9\xf62\x12r$', 115543857214536714816905432165802482622279954578813798680160907802237948487356, b"\xd3\xcau\x17\xfd'I\x89m\xdbY\xed\xd2\xc8\xe5j\xae\x9b\xb5\x08\xbf\x10O\x04B\x87\xce\xfcL\xd3\x08\xdb")

Proof verified: True
Proof generation time: 0.000009 seconds
Proof verification time: 0.000007 seconds
Proof size in memory: 72 bytes

Round 4:

Matrix A:
[8, 8, 2, 1, 9, 7, 6, 1, 1, 1]
[4, 9, 9, 5, 4, 6, 1, 4, 6, 4]
[5, 6, 5, 3, 5, 6, 5, 1, 4, 7]
[9, 5, 0, 1, 3, 3, 2, 4, 6, 1]
[0, 7, 1, 4, 9, 0, 2, 9, 1, 5]
[9, 5, 6, 6, 9, 7, 7, 6, 9, 2]
[1, 0, 0, 8, 8, 2, 0, 1, 9, 2]
[3, 2, 5, 0, 4, 4, 9, 4, 6, 6]
[7, 5, 8, 5, 9, 5, 7, 4, 7, 3]
[2, 1, 3, 2, 1, 3, 5, 5, 4, 4]

Matrix B:
[6, 4, 4, 1, 8, 0, 2, 6, 2, 6]
[5, 5, 9, 8, 2, 6, 1, 5, 5, 4]
[9, 8, 4, 1, 1, 6, 5, 5, 5, 9]
[6, 6, 5, 7, 2, 3, 2, 9, 8, 4]
[7, 3, 2, 7, 5, 5, 6, 9, 3, 9]
[3, 9, 8, 9, 5, 1, 0, 7, 0, 3]
[8, 3, 7, 0, 6, 4, 2, 5, 9, 2]
[9, 4, 9, 4, 1, 9, 3, 6, 8, 1]
[0, 3, 9, 9, 0, 9, 4, 6, 7, 8]
[2, 9, 8, 8, 0, 7, 0, 8, 1, 4]

Proof: (b'\xe1\x94\xa1\xc0\xb2\x1a\xd9nm\xa4\x08\x17\xee{\xed\xe4\xafe\xcb\x8ai\xe3gO\x14\xdd\xcb\xff\xc4\xb9\xaaJ', b'^\r\xcb\xc1\x9fxKq \xee\xa3\xcdM\xec\xc2\x90\x99\xca\xa6\xd3y\x90\x1b\x19\x02\x7f\xf1\xdcXIen', 17408926538890691166185193092664518687214588706841179674585113618572184803250, b'\r\xf5+4Y\xad6\'\xb8\xea&\xe8"Jo\x97\xa6y\xb7\x19\x13|\xf7\x8c\xfc\x02\xa9\xb8\x02\xb3\xfc\x80')

Proof verified: True
Proof generation time: 0.000020 seconds
Proof verification time: 0.000019 seconds
Proof size in memory: 72 bytes

Round 5:

Matrix A:
[3, 9, 2, 7, 5, 1, 9, 8, 1, 2, 5, 9, 5, 5, 6, 1, 0, 4, 5, 5]
[6, 2, 9, 5, 6, 5, 4, 8, 2, 8, 7, 0, 5, 1, 8, 7, 1, 4, 1, 8]
[8, 6, 2, 3, 9, 7, 1, 7, 7, 1, 3, 8, 4, 4, 9, 9, 7, 3, 9, 5]
[0, 6, 3, 6, 7, 1, 4, 2, 3, 6, 3, 2, 8, 4, 3, 6, 8, 3, 8, 5]
[9, 8, 4, 0, 5, 3, 7, 1, 2, 7, 1, 0, 8, 9, 1, 9, 8, 3, 1, 6]
[7, 9, 5, 9, 3, 3, 9, 1, 7, 3, 4, 1, 0, 0, 0, 1, 2, 1, 9, 8]
[9, 5, 1, 1, 4, 8, 9, 4, 5, 1, 0, 3, 5, 6, 9, 6, 3, 1, 9, 4]
[6, 1, 6, 1, 4, 4, 2, 1, 5, 3, 9, 5, 6, 0, 6, 3, 2, 6, 0, 8]
[6, 4, 1, 0, 8, 3, 6, 5, 1, 2, 9, 0, 4, 7, 8, 4, 3, 5, 4, 6]
[8, 8, 7, 7, 9, 6, 4, 3, 1, 3, 4, 6, 0, 2, 1, 4, 7, 8, 8, 1]
[6, 5, 0, 8, 2, 7, 6, 4, 2, 4, 2, 6, 0, 4, 2, 6, 9, 2, 3, 2]
[8, 3, 6, 6, 6, 0, 0, 2, 1, 8, 2, 3, 5, 3, 2, 3, 7, 7, 1, 1]
[4, 5, 8, 2, 2, 9, 0, 4, 4, 5, 9, 6, 8, 7, 4, 5, 5, 0, 1, 8]
[3, 8, 7, 4, 2, 7, 4, 4, 2, 4, 3, 5, 6, 7, 4, 6, 4, 5, 9, 0]
[6, 9, 3, 6, 0, 4, 0, 2, 6, 6, 3, 5, 9, 5, 7, 9, 3, 2, 5, 7]
[8, 3, 9, 5, 4, 1, 6, 0, 0, 4, 9, 9, 1, 5, 0, 1, 4, 2, 1, 1]
[4, 8, 1, 2, 7, 2, 8, 4, 3, 4, 0, 0, 7, 3, 4, 7, 1, 6, 0, 1]
[3, 5, 6, 0, 1, 0, 4, 3, 4, 3, 5, 3, 8, 1, 9, 3, 9, 0, 4, 3]
[1, 5, 2, 6, 9, 9, 5, 0, 6, 2, 4, 6, 5, 6, 9, 4, 9, 1, 0, 5]
[2, 6, 6, 0, 7, 6, 6, 4, 2, 9, 0, 2, 2, 8, 8, 2, 0, 2, 8, 9]

Matrix B:
[3, 1, 2, 0, 8, 6, 4, 0, 5, 1, 6, 5, 0, 9, 1, 0, 7, 9, 2, 2]
[8, 4, 5, 8, 9, 1, 7, 0, 2, 7, 3, 9, 4, 3, 8, 6, 7, 7, 4, 3]
[4, 9, 9, 1, 1, 0, 3, 2, 5, 6, 3, 4, 3, 5, 5, 0, 4, 9, 3, 5]
[4, 9, 4, 1, 9, 7, 7, 9, 8, 8, 9, 2, 6, 4, 4, 0, 5, 0, 6, 6]
[4, 1, 5, 2, 7, 8, 9, 3, 9, 0, 1, 4, 8, 1, 1, 5, 2, 8, 2, 5]
[9, 2, 7, 2, 7, 9, 3, 5, 1, 0, 4, 1, 1, 7, 5, 6, 6, 3, 8, 2]
[5, 6, 5, 4, 7, 2, 5, 3, 1, 7, 2, 0, 3, 3, 9, 7, 3, 4, 5, 5]
[5, 7, 3, 1, 7, 8, 0, 0, 3, 9, 6, 7, 0, 4, 5, 3, 0, 4, 5, 1]
[6, 6, 5, 7, 2, 2, 0, 6, 7, 2, 8, 3, 8, 1, 4, 4, 2, 0, 3, 6]
[4, 5, 4, 5, 3, 2, 5, 0, 2, 5, 4, 9, 3, 0, 0, 6, 5, 7, 6, 1]
[0, 3, 2, 0, 5, 5, 7, 6, 6, 1, 6, 3, 8, 2, 2, 6, 1, 4, 7, 4]
[7, 3, 7, 6, 6, 6, 7, 2, 8, 7, 3, 3, 4, 5, 1, 1, 9, 4, 2, 6]
[3, 2, 7, 2, 4, 0, 1, 1, 3, 9, 8, 0, 5, 8, 7, 8, 5, 3, 1, 7]
[4, 5, 7, 3, 2, 2, 4, 1, 5, 9, 5, 0, 5, 3, 5, 9, 3, 8, 6, 4]
[8, 0, 7, 9, 2, 1, 9, 0, 8, 4, 0, 7, 9, 1, 5, 0, 4, 7, 3, 6]
[4, 8, 0, 1, 5, 5, 2, 6, 1, 6, 5, 0, 7, 1, 7, 6, 8, 4, 1, 9]
[2, 7, 4, 6, 3, 3, 7, 1, 8, 0, 9, 3, 8, 1, 7, 1, 3, 0, 3, 8]
[4, 4, 3, 3, 0, 3, 9, 7, 2, 8, 3, 6, 9, 1, 4, 0, 5, 5, 8, 0]
[7, 7, 4, 1, 9, 8, 9, 1, 6, 2, 1, 9, 1, 9, 7, 9, 5, 1, 7, 1]
[4, 3, 0, 5, 6, 4, 4, 9, 0, 9, 2, 3, 5, 7, 5, 5, 6, 5, 5, 6]

Proof: (b'P#e\xebh\xa6\x83\xc2\xa9n\xfa\x88+&R\xe1\xe4\xb7\x949\xed\xb8\x02EA\x1237\x03L\xe1\xc4', b'G+\xf6\x82\xbd\xdc%\xf7F\x12\xa73\xc71\xces\\-c\xba\xfd\xdb\xd3i\xde\xda\xdc\xe4\xf1\xf6\xec\xc7', 28604636994091339801586551968148248471990240431469906650156117109366596263742, b'\xd8\xf3\xca]\xc8i"\x8a\x14$*\x7f{\r\xa0\x14\xfb\x14Gq\x9b\xde\xe6z\x04\xe1bDj\x17\xcbt')

Proof verified: True
Proof generation time: 0.000058 seconds
Proof verification time: 0.000055 seconds
Proof size in memory: 72 bytes