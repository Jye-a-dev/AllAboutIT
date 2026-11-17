# Previous input
a = input("Enter the string: ")
old = input("Enter the substring to replace: ")
new = input("Enter the replacement substring: ")

# Process
def replace_Substring(a, old, new):
    return a.replace(old, new)

# Post process
print("String after replacement:", replace_Substring(a, old, new))
