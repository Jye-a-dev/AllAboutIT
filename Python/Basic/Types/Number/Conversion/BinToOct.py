# Previous input
n1 = int(input("Enter binary number: "), 2)

# Process
def from_Binary_Octal(a):
    return oct(a)[2:]
# Post process
print("The octal representation is:", from_Binary_Octal(n1))
