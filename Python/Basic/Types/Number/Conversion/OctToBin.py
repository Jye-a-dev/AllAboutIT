# Previous input
n1 = int(input("Enter octal number: "), 8)

# Process
def from_Octal_Binary(a):
    return bin(a)[2:]
# Post process
print("The binary representation is:", from_Octal_Binary(n1))
    