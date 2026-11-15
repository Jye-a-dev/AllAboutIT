# Previous input
n1 = int(input("Enter hexadecimal number: "), 16)

# Process
def from_Hexadecimal_Binary(a):
    return bin(a)[2:]
# Post process
print("The binary representation is:", from_Hexadecimal_Binary(n1))
