# Previous input
n = int(input("Enter the number of lists to add: "))
# Process
def plus_lists(n):
    lists = []
    for i in range(n):
        l = input(f"Enter list {i + 1}: ")
        lists.append(l)
    return lists + [","]
# Post process
print("The combined list is:", plus_lists(n))