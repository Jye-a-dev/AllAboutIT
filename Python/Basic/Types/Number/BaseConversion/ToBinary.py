# Previous input
n = int(input("Enter decimal integer: "))

# Process
def to_Binary(n):
    if n < 0:
        return "-" + bin(abs(n))[2:]
    return bin(n)[2:]

# Post process
print("The binary representation is:", to_Binary(n))
