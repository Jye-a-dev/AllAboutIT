# Previous input
a = input("Enter the string: ")
width = int(input("Enter total width: "))
fillchar = input("Enter fill character: ")

# Process
def pad_Left(a, width, fillchar=" "):
    char = fillchar[0] if fillchar else " "
    return a.rjust(width, char)

# Post process
print("Left padded string:", pad_Left(a, width, fillchar))
