# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def normalize_Vector(v):
    mag = sum(x**2 for x in v)**0.5
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector")
    return [x / mag for x in v]

# Post process
print("Normalized vector:", normalize_Vector(v))
