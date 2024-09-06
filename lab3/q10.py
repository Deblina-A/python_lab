def print_8_segment_display(n):
    
    patterns = {
        '0': [" _ ", "|_|", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }
    
    for i in range(1, n + 1):
        digit = str(i % 10)  
        if i == n:  
            for row in range(3):
                print(patterns[digit][row])
        else: 
            for row in range(3):
                print(patterns[digit][row], end=" ")
            print()  

n = int(input("Enter the value of N (number of lines): "))

print_8_segment_display(n)
