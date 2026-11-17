# Previous input
strings = input("Enter strings separated by comma: ").split(",")
delimiter = input("Enter the delimiter: ")

# Process
def join_Strings(strings, delimiter):
    return delimiter.join(strings)

# Post process
print("Joined string:", join_Strings(strings, delimiter))
