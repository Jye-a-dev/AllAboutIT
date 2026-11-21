# Previous input
a1 = float(input("Enter first term a1: "))
r = float(input("Enter common ratio r: "))
n = int(input("Enter number of terms n: "))

# Process
def geometric_Series_Sum(a1, r, n):
    if n <= 0:
        return 0.0
    if r == 1:
        return a1 * n
    return a1 * (1 - r ** n) / (1 - r)

# Post process
print("Sum of geometric series:", geometric_Series_Sum(a1, r, n))
