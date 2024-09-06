a1 = 2
r = 3

num_terms = 6

print("The first 6 terms of the geometric sequence are:")
for n in range(num_terms):
    term = a1 * (r ** n)
    print(term)