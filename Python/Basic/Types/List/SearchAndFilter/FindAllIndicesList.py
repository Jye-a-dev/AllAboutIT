# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to find all indices: ").strip()

# Process
def find_All_Indices_List(a, item):
    return [i for i, x in enumerate(a) if x == item]

# Post process
print("All indices of element:", find_All_Indices_List(a, item))
