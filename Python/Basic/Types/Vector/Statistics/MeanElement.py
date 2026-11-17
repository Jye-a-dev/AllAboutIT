# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def mean_Vector_Element(v):
    if not v:
        raise ValueError("Cannot calculate mean of an empty vector")
    return sum(v) / len(v)

# Post process
print("Mean of vector elements:", mean_Vector_Element(v))
