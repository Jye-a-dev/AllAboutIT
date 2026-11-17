# Previous input
a = input("Enter the string: ")

# Process
def normalize_Spaces(a):
    return " ".join(a.split())

# Post process
print("Normalized spaces string:", normalize_Spaces(a))
