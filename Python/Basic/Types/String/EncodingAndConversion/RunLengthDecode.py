# Previous input
a = input("Enter encoded RLE string (e.g. 3A2B): ")

# Process
import re

def run_Length_Decode(a):
    matches = re.findall(r"(\d+)(\D)", a)
    return "".join(char * int(count) for count, char in matches)

# Post process
print("Decoded string from RLE:", run_Length_Decode(a))
