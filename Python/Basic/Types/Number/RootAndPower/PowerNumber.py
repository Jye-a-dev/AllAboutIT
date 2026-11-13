# Previous input
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# Process
def power_numbers(num1, num2):
    return num1 ** num2
# Post process
print("The power of", n1, "and", n2, "is:", power_numbers(n1, n2))