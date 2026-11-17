# Previous input
a = input("Enter the string: ")

# Process
def count_Uppercase(a):
    return sum(1 for c in a if c.isupper())

# Post process
print("Uppercase character count:", count_Uppercase(a))
