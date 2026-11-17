# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def magnitude_L1(v):
    return sum(abs(x) for x in v)

# Post process
print("Manhattan magnitude (L1):", magnitude_L1(v))
