# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def reverse_Vector(v):
    return list(reversed(v))

# Post process
print("Reversed vector:", reverse_Vector(v))
