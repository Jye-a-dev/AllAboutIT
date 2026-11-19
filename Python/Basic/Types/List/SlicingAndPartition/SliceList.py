# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
start = int(input("Enter start index: ").strip())
end = int(input("Enter end index: ").strip())
step = int(input("Enter step (default 1): ").strip() or "1")

# Process
def slice_List(a, start, end, step=1):
    if step == 0:
        step = 1
    return a[start:end:step]

# Post process
print("Sliced list:", slice_List(a, start, end, step))
