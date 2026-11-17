# Previous input
a = input("Enter the multi-line string: ")

# Process
def split_Lines(a):
    return a.splitlines()

# Post process
print("Lines list:", split_Lines(a))
