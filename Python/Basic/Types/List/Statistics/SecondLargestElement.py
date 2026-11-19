# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def find_Second_Largest(a):
    unique = sorted(set(a))
    if len(unique) < 2:
        return None
    return unique[-2]

# Post process
print("Second largest element in list:", find_Second_Largest(a))
