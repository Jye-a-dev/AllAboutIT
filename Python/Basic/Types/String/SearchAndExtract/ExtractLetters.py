# Previous input
a = input("Enter the string: ")

# Process
def extract_Letters(a):
    return "".join(c for c in a if c.isalpha())

# Post process
print("Extracted letters:", extract_Letters(a))
