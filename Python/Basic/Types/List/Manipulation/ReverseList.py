# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def reverse_List(a):
    return a[::-1]

# Post process
print("Reversed list:", reverse_List(a))
