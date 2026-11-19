# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def remove_Duplicate_Elements(a):
    seen = set()
    res = []
    for item in a:
        if item not in seen:
            seen.add(item)
            res.append(item)
    return res

# Post process
print("List after removing duplicates (preserving order):", remove_Duplicate_Elements(a))
