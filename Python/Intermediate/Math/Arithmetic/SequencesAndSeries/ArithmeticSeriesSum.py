# Previous input
a1 = int(input("Enter first term a1: "))
d = int(input("Enter common difference d: "))
n = int(input("Enter number of terms n: "))

# Process
def arithmetic_Series_Sum(a1, d, n):
    if n <= 0:
        return 0
    return (n * (2 * a1 + (n - 1) * d)) // 2

# Post process
print("Sum of arithmetic series:", arithmetic_Series_Sum(a1, d, n))
