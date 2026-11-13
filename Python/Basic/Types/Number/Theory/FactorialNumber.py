# Previous input
a = int(input("Enter the number to calculate factorial for: "))
# Process
def Factorial_Number(a):
    if a <= 0:
        return 0

    result = 1
    for i in range(1, a + 1):
        result *= i
    return result
# Post process
print("The factorial of the entered number is:", Factorial_Number(a))