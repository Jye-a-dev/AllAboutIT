# Previous input
n = int(input("Enter the number of vectors to subtract: "))
vectors = []
for i in range(n):
    v = [float(x) for x in input(f"Enter vector {i + 1} (comma-separated): ").split(",")]
    vectors.append(v)

# Process
def subtract_N_Vectors(vectors):
    if not vectors:
        return []
    dim = len(vectors[0])
    for v in vectors:
        if len(v) != dim:
            raise ValueError("All vectors must have the same dimension")
    res = list(vectors[0])
    for v in vectors[1:]:
        for i in range(dim):
            res[i] -= v[i]
    return res

# Post process
print("The difference of the entered vectors is:", subtract_N_Vectors(vectors))
