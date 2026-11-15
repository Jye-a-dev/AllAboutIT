# Previous input
n1 = int(input("Enter hexadecimal number: "), 16)

# Process
def from_Hexadecimal_Octal(a):
    return oct(a)[2:]
# Post process
print("The octal representation is:", from_Hexadecimal_Octal(n1))
