# Previous input
array = [8, 5, 3, 1, 7, 2, 6, 4]
# Process
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Post process
print("Sorted array:", bubble_sort(array.copy()))