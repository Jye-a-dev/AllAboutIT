# Previous input
a = input("Enter the string: ")

# Process
def to_Hex_String(a):
    return a.encode("utf-8").hex()

# Post process
print("Hex string:", to_Hex_String(a))
