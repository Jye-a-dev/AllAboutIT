# Previous input
a = input("Enter the string: ")

# Process
import string

def remove_Punctuation(a):
    return "".join(c for c in a if c not in string.punctuation)

# Post process
print("String without punctuation:", remove_Punctuation(a))
