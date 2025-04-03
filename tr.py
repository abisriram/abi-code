def find_original_time(matrix, N1, N2):
    # Correct positions of numbers in an ideal 5x5 analog clock
    correct_positions = {
        (0, 1): 11, (0, 2): 12, (0, 3): 1,
        (1, 0): 10, (1, 4): 2,
        (2, 0): 9,  (2, 4): 3,
        (3, 0): 8,  (3, 4): 4,
        (4, 1): 7,  (4, 2): 6,  (4, 3): 5
    }
    
    # Reverse mapping for easy lookup
    value_to_position = {v: k for k, v in correct_positions.items()}
    
    # Find where N1 and N2 are in the given matrix
    n1_pos = None
    n2_pos = None
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == N1:
                n1_pos = (i, j)
            if matrix[i][j] == N2:
                n2_pos = (i, j)
                print("n1 position is:",n1_pos)
                print("n2 position is:",n2_pos)
    
    # Get original hour and minute values
    original_hour = correct_positions.get(n1_pos, 12)  # Default to 12 if not found
    original_minute = correct_positions.get(n2_pos, 0) * 5  # Convert to minutes
    
    # Format and print time
    print(f"{original_hour:02}:{original_minute:02}")

                                 
# Input Processing
def main():
    
    matrix = []
    for _ in range(5):
        row = input().split()
        matrix.append([int(x) if x.isdigit() else 0 for x in row])
    
    N1, N2 = map(int, input().split())
    find_original_time(matrix, N1, N2)
    
if __name__ == "__main__":
    main()
