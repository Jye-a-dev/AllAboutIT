# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def filter_Negative_Numbers(a):
    return [x for x in a if x < 0]

# Post process
print("Filtered negative numbers:", filter_Negative_Numbers(a))
