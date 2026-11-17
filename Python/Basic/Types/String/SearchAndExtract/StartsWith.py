# Previous input
a = input("Enter the string: ")
prefix = input("Enter the prefix: ")

# Process
def starts_With(a, prefix):
    return a.startswith(prefix)

# Post process
print("Starts with prefix:", starts_With(a, prefix))
