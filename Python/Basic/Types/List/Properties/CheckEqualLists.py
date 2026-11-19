# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def is_Equal_Lists(a, b):
    return a == b

# Post process
print("The two lists are equal:", is_Equal_Lists(a, b))
