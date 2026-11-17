# Previous input
a = input("Enter the string: ")

# Process
def is_Alpha(a):
    return a.isalpha()

# Post process
print("Contains only alphabetic characters:", is_Alpha(a))
