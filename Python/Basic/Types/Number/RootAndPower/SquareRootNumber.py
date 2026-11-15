# Previous input
n1 = int(input("Enter square number: "))
n2 = int(input("Enter squared number: "))

# Process
def Square_Root_Number(a, b):
    return (a * b) ** 0.5

# Post process
print("The square root of the product of the entered numbers is:", Square_Root_Number(n1, n2))
