# Previous input
a = input("Enter the string: ")

# Process
def count_Lowercase(a):
    return sum(1 for c in a if c.islower())

# Post process
print("Lowercase character count:", count_Lowercase(a))
