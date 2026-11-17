# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def max_Vector_Element(v):
    if not v:
        raise ValueError("Cannot find maximum of an empty vector")
    return max(v)

# Post process
print("Maximum element:", max_Vector_Element(v))
