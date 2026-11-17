# Previous input
a = input("Enter binary string separated by spaces: ")

# Process
def from_Binary_String(a):
    parts = a.strip().split()
    chars = []
    for b in parts:
        try:
            chars.append(chr(int(b, 2)))
        except ValueError:
            pass
    return "".join(chars)

# Post process
print("Decoded string from binary:", from_Binary_String(a))
