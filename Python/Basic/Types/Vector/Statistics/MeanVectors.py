# Previous input
n = int(input("Enter the number of vectors: "))
vectors = []
for i in range(n):
    v = [float(x) for x in input(f"Enter vector {i + 1} (comma-separated): ").split(",")]
    vectors.append(v)

# Process
def mean_Vectors(vectors):
    if not vectors:
        raise ValueError("Vector list cannot be empty")
    dim = len(vectors[0])
    for v in vectors:
        if len(v) != dim:
            raise ValueError("All vectors must have the same dimension")
    return [sum(coords) / len(vectors) for coords in zip(*vectors)]

# Post process
print("Mean vector of entered vectors:", mean_Vectors(vectors))
