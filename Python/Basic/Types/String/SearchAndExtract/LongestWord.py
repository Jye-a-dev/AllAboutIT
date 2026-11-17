# Previous input
a = input("Enter the string: ")

# Process
import re

def find_Longest_Word(a):
    words = re.findall(r"\b\w+\b", a)
    if not words:
        return ""
    return max(words, key=len)

# Post process
print("Longest word:", find_Longest_Word(a))
