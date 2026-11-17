# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def get_Dimension(v):
    return len(v)

# Post process
print("Vector dimension:", get_Dimension(v))
