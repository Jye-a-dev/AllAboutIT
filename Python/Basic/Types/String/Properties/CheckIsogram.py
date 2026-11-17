# Previous input
a = input("Enter the string: ")

# Process
def is_Isogram(a):
    letters = [c.lower() for c in a if c.isalpha()]
    return len(letters) == len(set(letters))

# Post process
print("Is isogram:", is_Isogram(a))
