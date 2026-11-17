import math

# Previous input
v = [float(x) for x in input("Enter 2D vector (comma-separated): ").split(",")]
angle = float(input("Enter rotation angle in radians: "))

# Process
def rotate_Vector_2D(v, angle):
    if len(v) != 2:
        raise ValueError("Vector must be 2-dimensional")
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [v[0] * cos_a - v[1] * sin_a, v[0] * sin_a + v[1] * cos_a]

# Post process
print("Rotated 2D vector:", rotate_Vector_2D(v, angle))
