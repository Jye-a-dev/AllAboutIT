# Previous input
a = input("Enter the string: ")

# Process
def count_Words(a):
    return len(a.split())

# Post process
print("Word count:", count_Words(a))
