# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
n = int(input("Enter index (0-based): ").strip())

# Process
def get_Nth_Element(a, n):
    if -len(a) <= n < len(a):
        return a[n]
    return None

# Post process
print("The element at index is:", get_Nth_Element(a, n))
