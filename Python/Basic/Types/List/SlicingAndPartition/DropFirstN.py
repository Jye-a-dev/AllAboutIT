# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
n = int(input("Enter number of elements to drop: ").strip())

# Process
def drop_First_N(a, n):
    return a[max(0, n):]

# Post process
print("List after dropping elements:", drop_First_N(a, n))
