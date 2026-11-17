# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring: ")

# Process
def find_First_Index(a, sub):
    return a.find(sub)

# Post process
print("First index of substring:", find_First_Index(a, sub))
