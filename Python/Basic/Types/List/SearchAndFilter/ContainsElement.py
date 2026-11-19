# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to check: ").strip()

# Process
def contains_Element(a, item):
    return item in a

# Post process
print("Element is in list:", contains_Element(a, item))
