import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_sin(x, n):
    sine_sum = 0
    for i in range(n):

        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine_sum += term
    return sine_sum

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms in the series: "))

if n > 0:
    result = compute_sin(x, n)
    print(f"sin({x}) using {n} terms of the series is: {result}")
   
    print(f"Using math.sin({x}) = {math.sin(x)}")
else:
    print("Please enter a positive integer for n.")
