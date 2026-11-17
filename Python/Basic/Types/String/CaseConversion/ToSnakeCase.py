# Previous input
a = input("Enter the string: ")

# Process
import re

def to_Snake_Case(a):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", a)
    words = re.findall(r"[A-Za-z0-9]+", s)
    return "_".join(w.lower() for w in words)

# Post process
print("Snake case string:", to_Snake_Case(a))
