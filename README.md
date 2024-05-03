# Zero Knowledge Proof (ZKP) for Matrix Multiplication

This repository contains Python code implementing a Zero Knowledge Proof (ZKP) scheme for matrix multiplication. The code demonstrates how a prover can convince a verifier that they know the product of two matrices \( A \) and \( B \) without revealing the matrices themselves.

## Prerequisites

- Python 3.x
- Git

## How to Run

1. Clone the repository to your local machine:

    git clone https://github.com/your-username/zkp-matrix-multiplication.git


2. Navigate to the cloned repository directory:

    cd zkp-matrix-multiplication


3. Run the Python script:


4. The script will generate random matrices \( A \) and \( B \), perform matrix multiplication \( A \times B \), and output the result along with the verification message.

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
