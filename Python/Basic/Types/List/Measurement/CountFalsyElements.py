# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",")]

# Process
def count_Falsy_Elements(a):
    return sum(1 for x in a if not bool(x.strip()))

# Post process
print("Number of falsy elements:", count_Falsy_Elements(a))
