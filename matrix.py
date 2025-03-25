import numpy as np

# Function to input a matrix
def input_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Please enter the correct number of elements.")
            return None
        matrix.append(row)
    return np.array(matrix)

# Matrix Operations
def matrix_operations():
    rows, cols = map(int, input("Enter rows and columns of the matrix: ").split())

    # Input matrices
    print("Matrix A:")
    A = input_matrix(rows, cols)
    print("Matrix B:")
    B = input_matrix(rows, cols)

    if A is None or B is None:
        print("Invalid matrix input.")
        return

    # Matrix operations
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nAddition (A + B):")
    print(A + B)
    print("\nSubtraction (A - B):")
    print(A - B)
    print("\nMultiplication (A * B):")
    print(A @ B.T)  # Transposing B to make it valid for multiplication
    print("\nTranspose of Matrix A:")
    print(A.T)
    print("\nTranspose of Matrix B:")
    print(B.T)

# Run the matrix operations
matrix_operations()