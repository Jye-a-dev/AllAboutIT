# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring: ")

# Process
def find_Last_Index(a, sub):
    return a.rfind(sub)

# Post process
print("Last index of substring:", find_Last_Index(a, sub))
