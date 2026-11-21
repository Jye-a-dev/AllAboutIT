# Previous input
a1 = float(input("Enter first term a1: "))
r = float(input("Enter common ratio r: "))
n = int(input("Enter term index n (1-based): "))

# Process
def geometric_Progression_Term(a1, r, n):
    if n <= 0:
        raise ValueError("Index n must be >= 1")
    return a1 * (r ** (n - 1))

# Post process
print("N-th term of geometric progression:", geometric_Progression_Term(a1, r, n))
