# Previous input
a = input("Enter the string: ")

# Process
import re

def find_Shortest_Word(a):
    words = re.findall(r"\b\w+\b", a)
    if not words:
        return ""
    return min(words, key=len)

# Post process
print("Shortest word:", find_Shortest_Word(a))
