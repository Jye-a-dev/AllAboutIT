# Previous input
s = input("Enter octal string: ")

# Process
def from_Octal(octal_str):
    return int(octal_str.strip(), 8)

# Post process
print("The decimal integer is:", from_Octal(s))
