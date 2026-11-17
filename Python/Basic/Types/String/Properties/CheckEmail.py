# Previous input
a = input("Enter the email address: ")

# Process
import re

def is_Valid_Email(a):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, a.strip()))

# Post process
print("Is valid email:", is_Valid_Email(a))
