# Apply combination formula to obtain answer
# Possible to iterate through binary numbers with 1's == 
n = 40
r = 20

def factorial(num):
    iteration = 1
    for x in range(1, (num + 1)):
        iteration = x * iteration
    return iteration
    
print ((factorial(n)) / (factorial(r) * factorial(n - r)))