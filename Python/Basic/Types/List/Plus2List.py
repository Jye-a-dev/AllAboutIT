# Previous input
n1 = (input("Enter first list: "))
n2 = (input("Enter second list: "))
# Process
def add_lists(list1, list2):
    return list1 + list2 + [""]
# Post process
print("The combined list of", n1, "and", n2, "is:", add_lists(n1, n2))