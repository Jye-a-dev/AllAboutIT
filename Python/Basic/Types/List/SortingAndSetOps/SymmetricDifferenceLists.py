# Previous input
a = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
b = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def symmetric_Difference_Lists(a, b):
    set_a = set(a)
    set_b = set(b)
    res = []
    for item in a:
        if item not in set_b and item not in res:
            res.append(item)
    for item in b:
        if item not in set_a and item not in res:
            res.append(item)
    return res

# Post process
print("Symmetric difference of two lists:", symmetric_Difference_Lists(a, b))
