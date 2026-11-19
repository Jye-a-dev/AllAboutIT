# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to prepend: ").strip()

# Process
def prepend_Element(a, item):
    return [item] + list(a)

# Post process
print("List after prepending element:", prepend_Element(a, item))
