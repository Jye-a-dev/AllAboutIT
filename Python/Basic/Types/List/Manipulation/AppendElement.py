# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to append: ").strip()

# Process
def append_Element(a, item):
    return list(a) + [item]

# Post process
print("List after appending element:", append_Element(a, item))
