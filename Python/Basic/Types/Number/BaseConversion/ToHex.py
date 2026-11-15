# Previous input
n = int(input("Enter decimal integer: "))

# Process
def to_Hex(n):
    if n < 0:
        return "-" + hex(abs(n))[2:].upper()
    return hex(n)[2:].upper()

# Post process
print("The hexadecimal representation is:", to_Hex(n))
