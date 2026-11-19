# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
k = int(input("Enter number of positions to rotate left: ").strip())

# Process
def rotate_Left_List(a, k):
    if not a:
        return []
    k = k % len(a)
    return a[k:] + a[:k]

# Post process
print("List rotated left:", rotate_Left_List(a, k))
