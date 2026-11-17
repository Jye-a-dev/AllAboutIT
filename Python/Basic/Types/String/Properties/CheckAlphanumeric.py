# Previous input
a = input("Enter the string: ")

# Process
def is_Alphanumeric(a):
    return a.isalnum()

# Post process
print("Contains only alphanumeric characters:", is_Alphanumeric(a))
