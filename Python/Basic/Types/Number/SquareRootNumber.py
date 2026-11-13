# Previous input
n1 = int(input("Enter square number: "))
n2 = int(input("Enter squared number: "))
# Process
def SquareRoot_numbers(a, b):
    return (a * b) ** 0.5
# Post process
print("The square root of the product of the entered numbers is:", SquareRoot_numbers(n1, n2))