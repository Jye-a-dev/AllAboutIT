# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring to remove: ")

# Process
def remove_Substring(a, sub):
    return a.replace(sub, "") if sub else a

# Post process
print("String after removing substring:", remove_Substring(a, sub))
