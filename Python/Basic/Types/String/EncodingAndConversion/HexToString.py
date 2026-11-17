# Previous input
a = input("Enter hex string: ")

# Process
def from_Hex_String(a):
    clean_hex = "".join(a.strip().split())
    if len(clean_hex) % 2 != 0:
        clean_hex = "0" + clean_hex
    try:
        return bytes.fromhex(clean_hex).decode("utf-8", errors="replace")
    except ValueError:
        return ""

# Post process
print("Decoded string from hex:", from_Hex_String(a))
