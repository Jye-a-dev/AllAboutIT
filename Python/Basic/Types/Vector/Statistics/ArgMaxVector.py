# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def argmax_Vector(v):
    if not v:
        raise ValueError("Cannot compute argmax of an empty vector")
    return v.index(max(v))

# Post process
print("Index of maximum element (argmax):", argmax_Vector(v))
