# Previous input
a = [x.strip() for x in input("Enter strings (comma-separated): ").split(",") if x.strip()]

# Process
def sort_By_String_Length(a, reverse=False):
    return sorted(a, key=len, reverse=reverse)

# Post process
print("Strings sorted by length:", sort_By_String_Length(a))
