# Previous input
arr = 1234237634234
# Process
def count_digits(a):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count

# Post process

count = count_digits(arr)
print(f"The number {arr} has {count} digits.")