# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]
t = float(input("Enter interpolation parameter t (0.0 to 1.0): "))

# Process
def lerp_Vectors(v1, v2, t):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return [a + t * (b - a) for a, b in zip(v1, v2)]

# Post process
print("Linearly interpolated vector:", lerp_Vectors(v1, v2, t))
