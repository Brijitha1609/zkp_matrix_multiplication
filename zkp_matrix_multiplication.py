import time
from zkp_library import generate_proof, verify_proof, generate_random_matrix
import sys

def main():
    # Define parameters for multiple rounds of matrix multiplication
    round_sizes = [(2, 3), (3, 2), (5, 5), (10, 10), (20, 20)]
    num_rounds = 5

    for i in range(num_rounds):
        print(f"Round {i+1}:")
        rows, cols = round_sizes[i % len(round_sizes)]

        # Generate random matrices
        matrix_A = generate_random_matrix(rows, cols)
        matrix_B = generate_random_matrix(cols, rows)

        # Print the matrices
        print("\nMatrix A:")
        for row in matrix_A:
            print(row)

        print("\nMatrix B:")
        for row in matrix_B:
            print(row)

        # Generate proof
        start_time = time.time()
        proof = generate_proof(matrix_A, matrix_B)
        proof_generation_time = time.time() - start_time
        print("\nProof:", proof)

        # Verify proof
        start_time = time.time()
        valid = verify_proof(proof, matrix_A, matrix_B)
        proof_verification_time = time.time() - start_time
        print("\nProof verified:", valid)

        # Compute and print time complexity
        print(f"Proof generation time: {proof_generation_time:.6f} seconds")
        print(f"Proof verification time: {proof_verification_time:.6f} seconds")

        # Check size of proof in memory
        proof_size = sys.getsizeof(proof)
        print(f"Proof size in memory: {proof_size} bytes\n")

if __name__ == "__main__":
    main()

