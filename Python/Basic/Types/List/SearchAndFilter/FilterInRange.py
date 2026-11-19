# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]
min_val = float(input("Enter minimum value: ").strip())
max_val = float(input("Enter maximum value: ").strip())

# Process
def filter_In_Range(a, min_val, max_val):
    return [x for x in a if min_val <= x <= max_val]

# Post process
print("Filtered numbers in range:", filter_In_Range(a, min_val, max_val))
