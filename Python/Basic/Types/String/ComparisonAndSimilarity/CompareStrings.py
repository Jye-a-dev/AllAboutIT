# Previous input
a = input("Enter the first string: ")
b = input("Enter the second string: ")

# Process
def compare_Strings(a, b):
    if a == b:
        return 0
    return -1 if a < b else 1

# Post process
print("Comparison result:", compare_Strings(a, b))
