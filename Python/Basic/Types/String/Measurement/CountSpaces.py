# Previous input
a = input("Enter the string: ")

# Process
def count_Spaces(a):
    return sum(1 for c in a if c.isspace())

# Post process
print("Space count:", count_Spaces(a))
