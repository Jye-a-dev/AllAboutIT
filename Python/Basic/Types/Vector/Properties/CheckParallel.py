# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def is_Parallel(v1, v2, tolerance=1e-9):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    m1 = sum(x**2 for x in v1)**0.5
    m2 = sum(x**2 for x in v2)**0.5
    if m1 <= tolerance or m2 <= tolerance:
        return True
    dot = sum(a * b for a, b in zip(v1, v2))
    return abs(abs(dot) - (m1 * m2)) <= tolerance

# Post process
print("Are vectors parallel:", is_Parallel(v1, v2))
