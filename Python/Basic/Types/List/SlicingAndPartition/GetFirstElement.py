# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def get_First_Element(a):
    return a[0] if a else None

# Post process
print("The first element is:", get_First_Element(a))
