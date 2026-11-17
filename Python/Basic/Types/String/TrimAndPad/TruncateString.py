# Previous input
a = input("Enter the string: ")
max_length = int(input("Enter maximum length: "))

# Process
def truncate_String(a, max_length):
    if max_length < 0:
        return ""
    return a[:max_length]

# Post process
print("Truncated string:", truncate_String(a, max_length))
