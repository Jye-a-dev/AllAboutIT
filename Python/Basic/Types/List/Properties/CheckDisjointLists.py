# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def is_Disjoint_Lists(a, b):
    return len(set(a) & set(b)) == 0

# Post process
print("The two lists are disjoint (no common elements):", is_Disjoint_Lists(a, b))
