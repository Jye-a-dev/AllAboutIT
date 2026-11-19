# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def count_Truthy_Elements(a):
    return sum(1 for x in a if bool(x))

# Post process
print("Number of truthy elements:", count_Truthy_Elements(a))
