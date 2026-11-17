# Previous input
a = input("Enter the string: ")

# Process
import re
import unicodedata

def to_Slug(a):
    s = a.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

# Post process
print("Slug string:", to_Slug(a))
