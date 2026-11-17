# Previous input
a = input("Enter the string: ")

# Process
def count_Digits(a):
    return sum(1 for c in a if c.isdigit())

# Post process
print("Digit count:", count_Digits(a))
