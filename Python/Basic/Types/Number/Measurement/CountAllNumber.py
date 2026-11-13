# Previous input
arr = [1,5,2,1,3,5,1,4,2]
target_number = 1
# Process
def count_all_numbers(arr):
    for number in set(arr):
        count = arr.count(number)
        print(f"The number {number} appears {count} times in the array.")

# Post process

count = count_all_numbers(arr)
print(f"The number {target_number} appears {count} times in the array.")

