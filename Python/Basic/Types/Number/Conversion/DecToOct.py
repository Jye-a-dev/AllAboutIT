# Previous input
n1 = int(input("Enter decimal number: "))

# Process
def to_Octal(a):
    return oct(a)[2:]
# Post process
print("The octal representation is:", to_Octal(n1))
