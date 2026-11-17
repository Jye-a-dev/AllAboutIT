# Previous input
a = input("Enter the string: ")

# Process
def count_Special_Chars(a):
    return sum(1 for c in a if not c.isalnum() and not c.isspace())

# Post process
print("Special character count:", count_Special_Chars(a))
