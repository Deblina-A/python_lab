import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_cos(x, n):
    cos_sum = 0
    for i in range(n):
      
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_sum += term
    return cos_sum

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms in the series: "))

if n > 0:
    result = compute_cos(x, n)
    print(f"cos({x}) using {n} terms of the series is: {result}")
   
    print(f"Using math.cos({x}) = {math.cos(x)}")
else:
    print("Please enter a positive integer for n.")
