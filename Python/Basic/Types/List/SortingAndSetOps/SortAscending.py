# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def sort_Ascending(a):
    return sorted(a)

# Post process
print("List sorted in ascending order:", sort_Ascending(a))
