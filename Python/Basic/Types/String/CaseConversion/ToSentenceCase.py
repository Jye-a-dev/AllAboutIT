# Previous input
a = input("Enter the string: ")

# Process
import re

def to_Sentence_Case(a):
    if not a:
        return ""
    tokens = re.split(r"([.!?]\s*)", a)
    result = []
    for i in range(0, len(tokens), 2):
        s = tokens[i]
        if s:
            s = s[0].upper() + s[1:].lower()
        result.append(s)
        if i + 1 < len(tokens):
            result.append(tokens[i + 1])
    return "".join(result)

# Post process
print("Sentence case string:", to_Sentence_Case(a))
