# Previous input
a = input("Enter the string: ")
width = int(input("Enter total width: "))
fillchar = input("Enter fill character: ")

# Process
def center_String(a, width, fillchar=" "):
    char = fillchar[0] if fillchar else " "
    return a.center(width, char)

# Post process
print("Centered string:", center_String(a, width, fillchar))
