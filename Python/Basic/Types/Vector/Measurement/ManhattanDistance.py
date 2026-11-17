# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def manhattan_Distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return sum(abs(a - b) for a, b in zip(v1, v2))

# Post process
print("Manhattan distance:", manhattan_Distance(v1, v2))
