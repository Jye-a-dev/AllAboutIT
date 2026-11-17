# Previous input
v1 = [float(x) for x in input("Enter first 3D vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second 3D vector (comma-separated): ").split(",")]

# Process
def cross_Product_3D(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Both vectors must be 3-dimensional")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Post process
print("3D cross product:", cross_Product_3D(v1, v2))
