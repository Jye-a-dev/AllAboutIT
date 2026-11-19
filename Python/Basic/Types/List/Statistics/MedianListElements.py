# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def median_List_Elements(a):
    if not a:
        return 0.0
    s = sorted(a)
    n = len(s)
    mid = n // 2
    if n % 2 != 0:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2.0

# Post process
print("Median of list elements:", median_List_Elements(a))
