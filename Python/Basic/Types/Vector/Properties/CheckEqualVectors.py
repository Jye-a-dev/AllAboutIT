# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def is_Equal_Vectors(v1, v2, tolerance=1e-9):
    if len(v1) != len(v2):
        return False
    return all(abs(a - b) <= tolerance for a, b in zip(v1, v2))

# Post process
print("Are vectors equal:", is_Equal_Vectors(v1, v2))
