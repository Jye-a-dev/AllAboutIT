# Previous input
a = input("Enter the string: ")

# Process
def is_Numeric(a):
    return a.isnumeric()

# Post process
print("Contains only numeric characters:", is_Numeric(a))
