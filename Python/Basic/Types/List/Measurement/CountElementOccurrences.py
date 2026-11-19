# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
item = input("Enter the element to count: ").strip()

# Process
def count_Element_Occurrences(a, item):
    return a.count(item)

# Post process
print("Occurrences of element in list:", count_Element_Occurrences(a, item))
