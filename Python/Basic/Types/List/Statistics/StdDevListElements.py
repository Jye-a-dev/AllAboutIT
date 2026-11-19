# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def std_Dev_List_Elements(a):
    if len(a) < 2:
        return 0.0
    mean = sum(a) / len(a)
    variance = sum((x - mean) ** 2 for x in a) / len(a)
    return variance ** 0.5

# Post process
print("Standard deviation of list elements:", std_Dev_List_Elements(a))
