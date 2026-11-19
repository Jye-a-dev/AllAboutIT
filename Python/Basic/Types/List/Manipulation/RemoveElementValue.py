# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to remove: ").strip()

# Process
def remove_Element_Value(a, item):
    res = list(a)
    if item in res:
        res.remove(item)
    return res

# Post process
print("List after removing first occurrence:", remove_Element_Value(a, item))
