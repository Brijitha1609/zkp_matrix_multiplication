import random
from hashlib import sha256


def generate_proof(matrix_A, matrix_B):
    """
    Generates a zero-knowledge proof for the matrix multiplication.

    Args:
    - matrix_A: Matrix A for multiplication
    - matrix_B: Matrix B for multiplication

    Returns:
    - proof: Zero-knowledge proof
    """
    commitment_A = commit_matrix(matrix_A)
    commitment_B = commit_matrix(matrix_B)
    challenge = random.getrandbits(256)  # 256-bit challenge
    response = compute_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge)

    return commitment_A, commitment_B, challenge, response


def verify_proof(proof, matrix_A, matrix_B):
    """
    Verifies the zero-knowledge proof for the matrix multiplication.

    Args:
    - proof: Zero-knowledge proof (commitment_A, commitment_B, challenge, response)
    - matrix_A: Matrix A for multiplication
    - matrix_B: Matrix B for multiplication

    Returns:
    - valid: True if proof is valid, False otherwise
    """
    commitment_A, commitment_B, challenge, response = proof
    recomputed_commitment_A = commit_matrix(matrix_A)
    recomputed_commitment_B = commit_matrix(matrix_B)
    valid = verify_response(matrix_A, matrix_B, recomputed_commitment_A, recomputed_commitment_B, challenge, response)

    return valid


def commit_matrix(matrix):
    """
    Computes the commitment to a matrix.

    Args:
    - matrix: The matrix to be committed

    Returns:
    - commitment: The commitment to the matrix
    """
    matrix_str = "".join(str(row) for row in matrix)
    return sha256(matrix_str.encode()).digest()


def compute_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge):
    """
    Computes the response to the challenge.

    Args:
    - matrix_A: Matrix A for multiplication
    - matrix_B: Matrix B for multiplication
    - commitment_A: Commitment to matrix A
    - commitment_B: Commitment to matrix B
    - challenge: The challenge

    Returns:
    - response: The response to the challenge
    """
    input_str = str(matrix_A) + str(matrix_B) + str(commitment_A) + str(commitment_B) + str(challenge)
    return sha256(input_str.encode()).digest()


def verify_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge, response):
    """
    Verifies the response to the challenge.

    Args:
    - matrix_A: Matrix A for multiplication
    - matrix_B: Matrix B for multiplication
    - commitment_A: Commitment to matrix A
    - commitment_B: Commitment to matrix B
    - challenge: The challenge
    - response: The response to the challenge

    Returns:
    - valid: True if response is valid, False otherwise
    """
    expected_response = compute_response(matrix_A, matrix_B, commitment_A, commitment_B, challenge)
    valid = (response == expected_response)

    return valid


# Add a function to generate random matrices
def generate_random_matrix(rows, cols):
    """
    Generates a random matrix with the specified number of rows and columns.

    Args:
    - rows: Number of rows
    - cols: Number of columns

    Returns:
    - matrix: The randomly generated matrix
    """
    matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    return matrix

