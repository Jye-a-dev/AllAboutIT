# Previous input
u = [float(x) for x in input("Enter vector u (comma-separated): ").split(",")]
v = [float(x) for x in input("Enter vector v (comma-separated): ").split(",")]

# Process
def reject_Vector(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have the same dimension")
    dot_vv = sum(x**2 for x in v)
    if dot_vv == 0:
        raise ValueError("Cannot reject with respect to a zero vector")
    scalar = sum(a * b for a, b in zip(u, v)) / dot_vv
    return [a - b * scalar for a, b in zip(u, v)]

# Post process
print("Rejection of u from v:", reject_Vector(u, v))
