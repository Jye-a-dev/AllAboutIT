# Previous input
n = int(input("Enter decimal integer: "))

# Process
def to_Octal(n):
    if n < 0:
        return "-" + oct(abs(n))[2:]
    return oct(n)[2:]

# Post process
print("The octal representation is:", to_Octal(n))
