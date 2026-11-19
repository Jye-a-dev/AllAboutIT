# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def zip_2_Lists(a, b):
    return list(zip(a, b))

# Post process
print("Zipped pairs of two lists:", zip_2_Lists(a, b))
