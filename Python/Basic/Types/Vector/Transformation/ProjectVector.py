# Previous input
u = [float(x) for x in input("Enter vector u (comma-separated): ").split(",")]
v = [float(x) for x in input("Enter vector v to project onto (comma-separated): ").split(",")]

# Process
def project_Vector(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have the same dimension")
    dot_vv = sum(x**2 for x in v)
    if dot_vv == 0:
        raise ValueError("Cannot project onto a zero vector")
    scalar = sum(a * b for a, b in zip(u, v)) / dot_vv
    return [x * scalar for x in v]

# Post process
print("Projection of u onto v:", project_Vector(u, v))
