# Previous input
arr = 1234237634234
# Process
def count_bits(a):
    count = 0
    while a > 0:
        a //= 2
        count += 1
    return count

# Post process

count = count_bits(arr)
print(f"The number {arr} has {count} bits.")