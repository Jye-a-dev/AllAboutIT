# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def get_Last_Element(a):
    return a[-1] if a else None

# Post process
print("The last element is:", get_Last_Element(a))
