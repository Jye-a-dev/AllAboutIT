# Previous input
a = [x.strip() for x in input("Enter list elements (comma-separated): ").split(",")]

# Process
def remove_Falsy_Values(a):
    res = []
    for x in a:
        if not bool(x):
            continue
        if isinstance(x, str) and x.strip().lower() in ("", "0", "false", "none"):
            continue
        res.append(x)
    return res

# Post process
print("List after removing falsy values:", remove_Falsy_Values(a))
