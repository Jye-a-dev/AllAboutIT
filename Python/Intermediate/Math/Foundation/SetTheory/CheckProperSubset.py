# Previous input
a = [x.strip() for x in input("Enter elements of set A (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter elements of set B (comma-separated): ").split(",") if x.strip()]

# Process
def is_Proper_Subset(a, b):
    sa, sb = set(a), set(b)
    return sa < sb

# Post process
print("A is a proper subset of B:", is_Proper_Subset(a, b))
