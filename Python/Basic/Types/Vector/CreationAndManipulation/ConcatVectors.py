# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def concat_Vectors(v1, v2):
    return list(v1) + list(v2)

# Post process
print("Concatenated vector:", concat_Vectors(v1, v2))
