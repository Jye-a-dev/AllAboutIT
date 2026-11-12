# Previous input
n1 = (input("Enter first string: "))
n2 = (input("Enter second string: "))
# Process
def add_strings(str1, str2):
    return str1 + str2
# Post process
print("The combined string of", n1, "and", n2, "is:", add_strings(n1, n2))