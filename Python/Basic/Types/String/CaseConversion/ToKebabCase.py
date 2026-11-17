# Previous input
a = input("Enter the string: ")

# Process
import re

def to_Kebab_Case(a):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", a)
    words = re.findall(r"[A-Za-z0-9]+", s)
    return "-".join(w.lower() for w in words)

# Post process
print("Kebab case string:", to_Kebab_Case(a))
