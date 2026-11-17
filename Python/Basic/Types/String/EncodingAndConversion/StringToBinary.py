# Previous input
a = input("Enter the string: ")

# Process
def to_Binary_String(a):
    return " ".join(format(ord(c), "08b") for c in a)

# Post process
print("Binary representation:", to_Binary_String(a))
