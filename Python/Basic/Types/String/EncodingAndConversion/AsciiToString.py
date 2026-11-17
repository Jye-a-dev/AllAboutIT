# Previous input
ascii_list = [int(x.strip()) for x in input("Enter ASCII numbers separated by comma: ").split(",") if x.strip()]

# Process
def from_Ascii_List(ascii_list):
    return "".join(chr(code) for code in ascii_list)

# Post process
print("Decoded string from ASCII:", from_Ascii_List(ascii_list))
