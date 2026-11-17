# Previous input
a = input("Enter the string: ")

# Process
import re

def extract_Emails(a):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, a)

# Post process
print("Extracted emails:", extract_Emails(a))
