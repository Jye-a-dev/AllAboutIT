# Previous input
a1 = int(input("Enter first term a1: "))
d = int(input("Enter common difference d: "))
n = int(input("Enter term index n (1-based): "))

# Process
def arithmetic_Progression_Term(a1, d, n):
    if n <= 0:
        raise ValueError("Index n must be >= 1")
    return a1 + (n - 1) * d

# Post process
print("N-th term of arithmetic progression:", arithmetic_Progression_Term(a1, d, n))
