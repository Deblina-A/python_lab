import math
def print_factorial_series(N):
   
    for i in range(1, N + 1):
        factorial = math.factorial(i)
        print(factorial, end=', ' if i < N else '\n')

N = int(input("Enter the number of terms: "))

print("The series is:")
print_factorial_series(N)