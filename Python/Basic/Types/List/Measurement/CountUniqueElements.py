# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def count_Unique_Elements(a):
    return len(set(a))

# Post process
print("Number of unique elements:", count_Unique_Elements(a))
