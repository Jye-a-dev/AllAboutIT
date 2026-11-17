# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def is_Zero_Vector(v, tolerance=1e-9):
    return all(abs(x) <= tolerance for x in v)

# Post process
print("Is zero vector:", is_Zero_Vector(v))
