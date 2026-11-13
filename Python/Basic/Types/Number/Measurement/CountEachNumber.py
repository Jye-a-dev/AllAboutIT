# Previous input
arr = [1,5,2,1,3,5,1,4,2]
target_number = 1
# Process
def count_numbers(arr, target):
    return arr.count(target)

# Post process

count = count_numbers(arr, target_number)
print(f"The number {target_number} appears {count} times in the array.")

