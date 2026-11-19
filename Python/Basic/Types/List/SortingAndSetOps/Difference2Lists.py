# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def difference_2_Lists(a, b):
    set_b = set(b)
    seen = set()
    res = []
    for item in a:
        if item not in set_b and item not in seen:
            seen.add(item)
            res.append(item)
    return res

# Post process
print("Difference of two lists (A - B):", difference_2_Lists(a, b))
