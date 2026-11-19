# Previous input
n = int(input("Enter the number of lists to add: "))

# Process
def plus_lists(n):
    lists = []
    for i in range(n):
        l = [x.strip() for x in input(f"Enter list {i + 1} (comma-separated): ").split(",") if x.strip()]
        lists.extend(l)
    return lists

def add_N_Lists(lists):
    res = []
    for l in lists:
        res.extend(l)
    return res

plus_N_Lists = plus_lists

# Post process
print("The combined list is:", plus_lists(n))
