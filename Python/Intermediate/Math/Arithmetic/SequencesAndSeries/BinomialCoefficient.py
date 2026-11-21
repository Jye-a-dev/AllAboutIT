import math

# Previous input
n = int(input("Enter n: "))
k = int(input("Enter k: "))

# Process
def binomial_Coefficient(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return math.comb(n, k)

# Post process
print("Binomial coefficient C(n, k):", binomial_Coefficient(n, k))
