# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def count_List_Length(a):
    return len(a)

# Post process
print("The length of the list is:", count_List_Length(a))
