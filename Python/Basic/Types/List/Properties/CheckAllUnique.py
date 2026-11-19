# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def is_All_Unique(a):
    return len(a) == len(set(a))

# Post process
print("All elements in the list are unique:", is_All_Unique(a))
