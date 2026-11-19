import random

# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def shuffle_List(a):
    res = list(a)
    random.shuffle(res)
    return res

# Post process
print("Shuffled list:", shuffle_List(a))
