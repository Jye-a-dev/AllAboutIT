# Previous input
n1 = int(input("Enter decimal number: "))

# Process
def to_Binary(a):
    return bin(a)[2:]

# Post process
print("The binary representation is:", to_Binary(n1))
