# Previous input
from Python.Basic.Types.Number.Properties.CheckPrimeNumber import is_Prime
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Process
def Prime_In_Range(a, b):
    start, end = sorted((a, b))
    return [value for value in range(start, end + 1) if is_Prime(value)]

# Post process
print("The prime numbers in the range are:", Prime_In_Range(n1, n2))
