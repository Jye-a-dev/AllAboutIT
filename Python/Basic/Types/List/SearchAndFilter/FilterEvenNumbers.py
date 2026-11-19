# Previous input
a = [int(x.strip()) for x in input("Enter integers (comma-separated): ").split(",") if x.strip()]

# Process
def filter_Even_Numbers(a):
    return [x for x in a if x % 2 == 0]

# Post process
print("Filtered even numbers:", filter_Even_Numbers(a))
