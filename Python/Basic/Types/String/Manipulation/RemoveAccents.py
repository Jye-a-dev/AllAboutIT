# Previous input
a = input("Enter the string: ")

# Process
import unicodedata

def remove_Accents(a):
    s = a.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))

# Post process
print("String without accents:", remove_Accents(a))
