# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def negate_Vector(v):
    return [-x for x in v]

# Post process
print("Negated vector:", negate_Vector(v))
