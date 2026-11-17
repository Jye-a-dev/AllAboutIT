# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def magnitude_L2(v):
    return sum(x**2 for x in v)**0.5

# Post process
print("Euclidean magnitude (L2):", magnitude_L2(v))
