# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def variance_List_Elements(a):
    if len(a) < 2:
        return 0.0
    mean = sum(a) / len(a)
    return sum((x - mean) ** 2 for x in a) / len(a)

# Post process
print("Variance of list elements:", variance_List_Elements(a))
