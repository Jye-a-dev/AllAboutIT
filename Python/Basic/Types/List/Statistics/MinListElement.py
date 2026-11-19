# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def min_List_Element(a):
    return min(a) if a else None

# Post process
print("Minimum element in list:", min_List_Element(a))
