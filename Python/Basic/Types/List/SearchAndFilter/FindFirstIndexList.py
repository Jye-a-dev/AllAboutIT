# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter element to find: ").strip()

# Process
def find_First_Index_List(a, item):
    try:
        return a.index(item)
    except ValueError:
        return -1

# Post process
print("First index of element:", find_First_Index_List(a, item))
