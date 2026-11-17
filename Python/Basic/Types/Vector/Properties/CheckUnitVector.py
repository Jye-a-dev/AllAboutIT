# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def is_Unit_Vector(v, tolerance=1e-9):
    mag = sum(x**2 for x in v)**0.5
    return abs(mag - 1.0) <= tolerance

# Post process
print("Is unit vector:", is_Unit_Vector(v))
