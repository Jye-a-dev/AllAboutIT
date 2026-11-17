# Previous input
v = [float(x) for x in input("Enter incident vector v (comma-separated): ").split(",")]
n = [float(x) for x in input("Enter normal vector n (comma-separated): ").split(",")]

# Process
def reflect_Vector(v, n):
    if len(v) != len(n):
        raise ValueError("Vectors must have the same dimension")
    dot_nn = sum(x**2 for x in n)
    if dot_nn == 0:
        raise ValueError("Normal vector cannot be a zero vector")
    scalar = 2.0 * sum(a * b for a, b in zip(v, n)) / dot_nn
    return [a - b * scalar for a, b in zip(v, n)]

# Post process
print("Reflected vector:", reflect_Vector(v, n))
