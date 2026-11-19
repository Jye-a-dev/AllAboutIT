# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def cartesian_Product_Lists(a, b):
    return [(x, y) for x in a for y in b]

# Post process
print("Cartesian product of two lists:", cartesian_Product_Lists(a, b))
