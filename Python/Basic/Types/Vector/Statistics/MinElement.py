# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def min_Vector_Element(v):
    if not v:
        raise ValueError("Cannot find minimum of an empty vector")
    return min(v)

# Post process
print("Minimum element:", min_Vector_Element(v))
