# Previous input
n1 = int(input("Enter decimal number: "))

# Process
def to_Hexadecimal(a):
    return hex(a)[2:].upper()
# Post process
print("The hexadecimal representation is:", to_Hexadecimal(n1))
