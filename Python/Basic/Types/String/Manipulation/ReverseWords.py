# Previous input
a = input("Enter the string: ")

# Process
def reverse_Words(a):
    return " ".join(a.split()[::-1])

# Post process
print("Words reversed:", reverse_Words(a))
