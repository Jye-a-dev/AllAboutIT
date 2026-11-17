# Previous input
a = input("Enter the string: ")
width = int(input("Enter total width: "))
fillchar = input("Enter fill character: ")

# Process
def pad_Right(a, width, fillchar=" "):
    char = fillchar[0] if fillchar else " "
    return a.ljust(width, char)

# Post process
print("Right padded string:", pad_Right(a, width, fillchar))
