# Previous input
s = input("Enter hexadecimal string: ")

# Process
def from_Hex(hex_str):
    return int(hex_str.strip(), 16)

# Post process
print("The decimal integer is:", from_Hex(s))
