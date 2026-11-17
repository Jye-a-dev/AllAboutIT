# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def is_Orthogonal(v1, v2, tolerance=1e-9):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    dot = sum(a * b for a, b in zip(v1, v2))
    return abs(dot) <= tolerance

# Post process
print("Are vectors orthogonal:", is_Orthogonal(v1, v2))
