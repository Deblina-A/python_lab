def sum_of_digits(number):
   
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a number to find the sum of its digits: "))

result = sum_of_digits(number)

print(f"The sum of the digits of {number} is {result}")