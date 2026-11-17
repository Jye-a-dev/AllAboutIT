# Previous input
v1 = [float(x) for x in input("Enter first 2D vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second 2D vector (comma-separated): ").split(",")]

# Process
def cross_Product_2D(v1, v2):
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError("Both vectors must be 2-dimensional")
    return v1[0] * v2[1] - v1[1] * v2[0]

# Post process
print("2D cross product (determinant):", cross_Product_2D(v1, v2))
