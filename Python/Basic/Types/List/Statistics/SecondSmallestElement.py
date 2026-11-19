# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def find_Second_Smallest(a):
    unique = sorted(set(a))
    if len(unique) < 2:
        return None
    return unique[1]

# Post process
print("Second smallest element in list:", find_Second_Smallest(a))
