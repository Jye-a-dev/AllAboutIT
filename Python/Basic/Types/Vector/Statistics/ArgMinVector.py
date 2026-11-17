# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def argmin_Vector(v):
    if not v:
        raise ValueError("Cannot compute argmin of an empty vector")
    return v.index(min(v))

# Post process
print("Index of minimum element (argmin):", argmin_Vector(v))
