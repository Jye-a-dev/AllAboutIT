# Previous input
a = input("Enter the string: ")

# Process
def trim_Left(a):
    return a.lstrip()

# Post process
print("Left trimmed string:", trim_Left(a))
