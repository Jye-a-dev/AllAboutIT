# Previous input
a = input("Enter the string: ")
n = int(input("Enter chunk size: "))

# Process
def split_Chunks(a, n):
    if n <= 0:
        return []
    return [a[i:i + n] for i in range(0, len(a), n)]

# Post process
print("Chunks list:", split_Chunks(a, n))
