# Previous input
a = input("Enter the string: ")
delimiter = input("Enter the delimiter: ")

# Process
def split_By_Delimiter(a, delimiter):
    return a.split(delimiter)

# Post process
print("Split list:", split_By_Delimiter(a, delimiter))
