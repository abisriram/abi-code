def sort_3x3_submatrices(matrix, R, C):
    # Traverse each 3x3 submatrix
    for i in range(0, R, 3):
        for j in range(0, C, 3):
            
            # Extract 3x3 submatrix elements
            submatrix = []
            for x in range(3):
                for y in range(3):
                    submatrix.append(matrix[i + x][j + y])

            # Sort the submatrix elements
            submatrix.sort()

            # Put sorted values back into the matrix
            idx = 0
            for x in range(3):
                for y in range(3):
                    matrix[i + x][j + y] = submatrix[idx]
                    idx += 1

# Read input
R, C = map(int, input().split())  # Read R and C
matrix = [list(map(int, input().strip())) for _ in range(R)]  # Read matrix

# Process the matrix
sort_3x3_submatrices(matrix, R, C)

# Print output
for row in matrix:
    print(" ".join(map(str, row)))

