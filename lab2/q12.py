number = int(input("Enter a number: "))

print(f"Multiplication table for {number} is:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")