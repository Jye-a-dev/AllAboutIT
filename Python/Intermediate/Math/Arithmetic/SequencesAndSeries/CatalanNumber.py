import math

# Previous input
n = int(input("Enter non-negative integer n: "))

# Process
def catalan_Number(n):
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)

# Post process
print("Catalan number C_n:", catalan_Number(n))
