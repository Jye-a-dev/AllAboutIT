# Previous input
n1 = int(input("Enter first number (dividend): "))
n2 = int(input("Enter second number (divisor): "))

# Process
def modulo_2_Numbers(a, b):
    return a % b

# Post process
print("The modulo of", n1, "and", n2, "is:", modulo_2_Numbers(n1, n2))
