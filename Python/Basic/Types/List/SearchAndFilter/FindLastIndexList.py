# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to find: ").strip()

# Process
def find_Last_Index_List(a, item):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == item:
            return i
    return -1

# Post process
print("Last index of element:", find_Last_Index_List(a, item))
