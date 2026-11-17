# Previous input
a = input("Enter the string: ")

# Process
import string

def is_Pangram(a):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(a.lower()))

# Post process
print("Is pangram:", is_Pangram(a))
