# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def sort_Descending(a):
    return sorted(a, reverse=True)

# Post process
print("List sorted in descending order:", sort_Descending(a))
