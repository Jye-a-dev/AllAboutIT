# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def is_Same_Dimension(v1, v2):
    return len(v1) == len(v2)

# Post process
print("Have same dimension:", is_Same_Dimension(v1, v2))
