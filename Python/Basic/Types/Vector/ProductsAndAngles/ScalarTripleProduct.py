# Previous input
v1 = [float(x) for x in input("Enter first 3D vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second 3D vector (comma-separated): ").split(",")]
v3 = [float(x) for x in input("Enter third 3D vector (comma-separated): ").split(",")]

# Process
def scalar_Triple_Product(v1, v2, v3):
    if len(v1) != 3 or len(v2) != 3 or len(v3) != 3:
        raise ValueError("All vectors must be 3-dimensional")
    cp = [
        v2[1] * v3[2] - v2[2] * v3[1],
        v2[2] * v3[0] - v2[0] * v3[2],
        v2[0] * v3[1] - v2[1] * v3[0]
    ]
    return sum(a * b for a, b in zip(v1, cp))

# Post process
print("Scalar triple product:", scalar_Triple_Product(v1, v2, v3))
