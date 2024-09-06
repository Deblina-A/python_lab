def print_spiral_pattern(n):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define directions for movement: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Starting position and direction index
    x, y = 0, 0
    direction_index = 0
    
    for num in range(1, n * n + 1):
        matrix[x][y] = num
        # Move to the next position
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]
        
        # Check if the next position is within bounds and not yet filled
        if (0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 0):
            x, y = next_x, next_y
        else:
            # Change direction
            direction_index = (direction_index + 1) % 4
            x += directions[direction_index][0]
            y += directions[direction_index][1]
        
    # Print the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Input from the user
n = int(input("Enter the value of N (number of lines): "))

# Call the function to print the pattern
print_spiral_pattern(n)
