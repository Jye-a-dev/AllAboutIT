# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring: ")

# Process
def contains_Substring(a, sub):
    return sub in a

# Post process
print("Contains substring:", contains_Substring(a, sub))
