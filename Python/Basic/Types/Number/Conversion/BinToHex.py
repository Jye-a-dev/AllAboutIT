# Previous input
n1 = int(input("Enter binary number: "), 2)

# Process
def from_Binary_Hexadecimal(a):
    return hex(a)[2:].upper()
# Post process
print("The binary representation is:", from_Binary_Hexadecimal(n1))
    