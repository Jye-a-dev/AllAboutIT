# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def sum_Vector_Elements(v):
    return sum(v)

# Post process
print("Sum of vector elements:", sum_Vector_Elements(v))
