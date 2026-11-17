# Previous input
a = input("Enter the identifier: ")

# Process
def is_Valid_Identifier(a):
    return a.isidentifier()

# Post process
print("Is valid identifier:", is_Valid_Identifier(a))
