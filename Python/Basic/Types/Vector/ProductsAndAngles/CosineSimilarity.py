# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def cosine_Similarity(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    m1 = sum(x**2 for x in v1)**0.5
    m2 = sum(x**2 for x in v2)**0.5
    if m1 == 0 or m2 == 0:
        raise ValueError("Cannot calculate cosine similarity with a zero vector")
    return sum(a * b for a, b in zip(v1, v2)) / (m1 * m2)

# Post process
print("Cosine similarity:", cosine_Similarity(v1, v2))
