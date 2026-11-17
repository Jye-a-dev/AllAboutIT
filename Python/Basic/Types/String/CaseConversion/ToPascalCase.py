# Previous input
a = input("Enter the string: ")

# Process
import re

def to_Pascal_Case(a):
    words = re.findall(r"[A-Za-z0-9]+", a)
    return "".join(w.capitalize() for w in words)

# Post process
print("Pascal case string:", to_Pascal_Case(a))
