# Previous input
n1 = [x.strip() for x in input("Enter first list (comma-separated): ").split(",") if x.strip()]
n2 = [x.strip() for x in input("Enter second list (comma-separated): ").split(",") if x.strip()]

# Process
def add_lists(list1, list2):
    return list(list1) + list(list2)

add_2_Lists = add_lists

# Post process
print("The combined list of", n1, "and", n2, "is:", add_lists(n1, n2))
