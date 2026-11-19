# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
k = int(input("Enter number of positions to rotate right: ").strip())

# Process
def rotate_Right_List(a, k):
    if not a:
        return []
    k = k % len(a)
    return a[-k:] + a[:-k] if k != 0 else list(a)

# Post process
print("List rotated right:", rotate_Right_List(a, k))
