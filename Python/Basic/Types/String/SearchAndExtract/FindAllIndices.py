# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring: ")

# Process
def find_All_Indices(a, sub):
    if not sub:
        return []
    indices = []
    start = 0
    while True:
        idx = a.find(sub, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    return indices

# Post process
print("All indices of substring:", find_All_Indices(a, sub))
