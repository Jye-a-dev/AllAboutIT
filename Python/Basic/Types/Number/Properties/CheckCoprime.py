# Previous input
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Process
def is_Coprime(a, b):
    while b:
        a, b = b, a % b
    return abs(a) == 1

# Post process
print("The entered numbers are coprime:", is_Coprime(n1, n2))
