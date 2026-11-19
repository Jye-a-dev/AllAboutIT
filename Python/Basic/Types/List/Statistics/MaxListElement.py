# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def max_List_Element(a):
    return max(a) if a else None

# Post process
print("Maximum element in list:", max_List_Element(a))
