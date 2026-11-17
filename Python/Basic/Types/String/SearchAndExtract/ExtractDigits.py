# Previous input
a = input("Enter the string: ")

# Process
def extract_Digits(a):
    return "".join(c for c in a if c.isdigit())

# Post process
print("Extracted digits:", extract_Digits(a))
