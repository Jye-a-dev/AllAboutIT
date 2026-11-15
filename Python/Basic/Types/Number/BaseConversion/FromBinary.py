# Previous input
s = input("Enter binary string: ")

# Process
def from_Binary(binary_str):
    return int(binary_str.strip(), 2)

# Post process
print("The decimal integer is:", from_Binary(s))
