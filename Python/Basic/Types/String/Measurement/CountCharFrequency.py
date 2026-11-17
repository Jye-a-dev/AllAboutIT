# Previous input
a = input("Enter the string: ")

# Process
def count_Char_Frequency(a):
    freq = {}
    for c in a:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Post process
print("Character frequency:", count_Char_Frequency(a))
