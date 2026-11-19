# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
index = int(input("Enter index to insert at: ").strip())
item = input("Enter element to insert: ").strip()

# Process
def insert_Element_At(a, index, item):
    res = list(a)
    res.insert(index, item)
    return res

# Post process
print("List after inserting element:", insert_Element_At(a, index, item))
