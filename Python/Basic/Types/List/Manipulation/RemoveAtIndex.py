# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
index = int(input("Enter index to remove: ").strip())

# Process
def remove_At_Index(a, index):
    if not a or index < -len(a) or index >= len(a):
        return list(a)
    res = list(a)
    res.pop(index)
    return res

# Post process
print("List after removing element at index:", remove_At_Index(a, index))
