# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def sum_List_Elements(a):
    return sum(a)

# Post process
print("Sum of list elements:", sum_List_Elements(a))
