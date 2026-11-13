# Previous input
arr = 1234237634234
# Process
def count_bytes(a):
    count = 0
    while a > 0:
        a //= 256
        count += 1
    return count

# Post process

count = count_bytes(arr)
print(f"The number {arr} has {count} bytes.")