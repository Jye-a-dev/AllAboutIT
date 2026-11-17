# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]
min_val = float(input("Enter minimum bound: "))
max_val = float(input("Enter maximum bound: "))

# Process
def clamp_Vector(v, min_val, max_val):
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val")
    return [max(min_val, min(max_val, x)) for x in v]

# Post process
print("Clamped vector:", clamp_Vector(v, min_val, max_val))
