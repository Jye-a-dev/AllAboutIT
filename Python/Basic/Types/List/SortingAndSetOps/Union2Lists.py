# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def union_2_Lists(a, b):
    seen = set()
    res = []
    for item in list(a) + list(b):
        if item not in seen:
            seen.add(item)
            res.append(item)
    return res

# Post process
print("Union of two lists:", union_2_Lists(a, b))
