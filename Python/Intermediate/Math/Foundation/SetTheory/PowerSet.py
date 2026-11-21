import itertools

# Previous input
s = [x.strip() for x in input("Enter set elements (comma-separated): ").split(",") if x.strip()]

# Process
def power_Set(s):
    elems = list(dict.fromkeys(s))
    res = []
    for r in range(len(elems) + 1):
        for combo in itertools.combinations(elems, r):
            res.append(list(combo))
    return res

# Post process
print("Power set of S:", power_Set(s))
