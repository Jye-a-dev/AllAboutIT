# Previous input
a = input("Enter the string: ")

# Process
def remove_Duplicate_Chars(a):
    seen = set()
    result = []
    for c in a:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)

# Post process
print("String without duplicates:", remove_Duplicate_Chars(a))
