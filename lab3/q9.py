def print_pattern(n):
    for i in range(1, n + 1):
        
        print(" " * (n - i) + ".")
       
        for j in range(1, i + 1):
            if j == 1:
                print(" " * (n - i) + "/" + " " * (2 * (j - 1)) + "\\")
            else:
                print(" " * (n - i) + "/" + "_" * (2 * (j - 1)) + "\\")
        print()  


n = int(input("Enter the value of N (number of triangles): "))

print_pattern(n)