# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
old_item = input("Enter old element: ").strip()
new_item = input("Enter new element: ").strip()

# Process
def replace_Element_Value(a, old_item, new_item):
    return [new_item if x == old_item else x for x in a]

# Post process
print("List after replacing element:", replace_Element_Value(a, old_item, new_item))
