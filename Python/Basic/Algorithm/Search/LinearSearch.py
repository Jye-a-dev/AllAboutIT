# Previous input
array = [5, 3, 8, 6, 2, 7, 4, 1]
target = 3
# Process
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
# Post process
print("The index of", target, "in the array is:", linear_search(array, target))