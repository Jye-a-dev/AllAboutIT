# Previous input
a = input("Enter the string: ")

# Process
def to_Ascii_List(a):
    return [ord(c) for c in a]

# Post process
print("ASCII values list:", to_Ascii_List(a))
