# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring: ")

# Process
def count_Substring(a, sub):
    return a.count(sub) if sub else 0

# Post process
print("Substring occurrence count:", count_Substring(a, sub))
