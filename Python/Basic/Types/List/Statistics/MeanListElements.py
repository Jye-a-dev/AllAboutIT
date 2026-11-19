# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def mean_List_Elements(a):
    if not a:
        return 0.0
    return sum(a) / len(a)

# Post process
print("Mean of list elements:", mean_List_Elements(a))
