# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to remove completely: ").strip()

# Process
def remove_All_Occurrences(a, item):
    return [x for x in a if x != item]

# Post process
print("List after removing all occurrences:", remove_All_Occurrences(a, item))
