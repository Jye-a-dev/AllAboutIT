# Previous input
a = input("Enter the string: ")

# Process
import re

def to_Camel_Case(a):
    words = re.findall(r"[A-Za-z0-9]+", a)
    if not words:
        return ""
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])

# Post process
print("Camel case string:", to_Camel_Case(a))
