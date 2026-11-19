# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def is_Empty_List(a):
    return len(a) == 0

# Post process
print("The list is empty:", is_Empty_List(a))
