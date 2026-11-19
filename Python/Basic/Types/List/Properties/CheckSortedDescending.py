# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def is_Sorted_Descending(a):
    return all(a[i] >= a[i + 1] for i in range(len(a) - 1))

# Post process
print("The list is sorted in descending order:", is_Sorted_Descending(a))
