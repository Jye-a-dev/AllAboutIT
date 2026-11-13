# Previous input
n1 = int(input("Enter square number: "))
n2 = int(input("Enter squared number: "))
# Process
def N_Root_numbers(a, b):
    return (a * b) ** (1 / b)
# Post process
print("The nth root of the product of the entered numbers is:", N_Root_numbers(n1, n2))