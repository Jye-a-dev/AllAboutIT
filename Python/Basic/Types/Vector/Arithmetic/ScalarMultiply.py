# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]
k = float(input("Enter scalar value: "))

# Process
def scalar_Multiply(v, k):
    return [x * k for x in v]

# Post process
print("Scalar multiplied vector:", scalar_Multiply(v, k))
