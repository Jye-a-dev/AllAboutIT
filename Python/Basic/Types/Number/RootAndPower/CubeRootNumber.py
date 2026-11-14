# Previous input
n1 = int(input("Enter square number: "))
n2 = int(input("Enter squared number: "))
# Process
def CubeRoot_numbers(a, b):
    return (a * b) ** (1/3)
# Post process
print("The cube root of the product of the entered numbers is:", CubeRoot_numbers(n1, n2))