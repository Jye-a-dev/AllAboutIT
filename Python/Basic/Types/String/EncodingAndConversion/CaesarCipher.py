# Previous input
a = input("Enter the string: ")
shift = int(input("Enter shift value: "))

# Process
def caesar_Cipher(a, shift):
    result = []
    for c in a:
        if c.isupper():
            result.append(chr((ord(c) - 65 + shift) % 26 + 65))
        elif c.islower():
            result.append(chr((ord(c) - 97 + shift) % 26 + 97))
        else:
            result.append(c)
    return "".join(result)

# Post process
print("Encrypted string with Caesar cipher:", caesar_Cipher(a, shift))
