def compute_series_sum(n):
    
    total_sum = 0
    
   
    for i in range(1, n + 1):
        
        if i % 2 == 0:
            total_sum -= 1 / i
        else:
            total_sum += 1 / i
    
    return total_sum

#
n = int(input("Enter a positive integer n: "))


if n > 0:
    result = compute_series_sum(n)
    print(f"The sum of the series up to {n} terms is: {result}")
else:
    print("Please enter a positive integer.")

