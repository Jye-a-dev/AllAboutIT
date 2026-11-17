# Previous input
a = input("Enter the string: ")

# Process
import re

def extract_Urls(a):
    pattern = r"https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_+.~#?&/=]*)"
    return re.findall(pattern, a)

# Post process
print("Extracted URLs:", extract_Urls(a))
