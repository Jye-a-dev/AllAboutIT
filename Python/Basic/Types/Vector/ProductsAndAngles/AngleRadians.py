import math

# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def angle_Between_Radians(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    m1 = sum(x**2 for x in v1)**0.5
    m2 = sum(x**2 for x in v2)**0.5
    if m1 == 0 or m2 == 0:
        raise ValueError("Cannot calculate angle with a zero vector")
    cos_theta = sum(a * b for a, b in zip(v1, v2)) / (m1 * m2)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    return math.acos(cos_theta)

# Post process
print("Angle between vectors in radians:", angle_Between_Radians(v1, v2))
