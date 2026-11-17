# Previous input
strings = input("Enter strings separated by comma: ").split(",")

# Process
def longest_Common_Suffix(strings):
    if not strings:
        return ""
    suffix = strings[0].strip()
    for s in strings[1:]:
        s = s.strip()
        while not s.endswith(suffix):
            suffix = suffix[1:]
            if not suffix:
                return ""
    return suffix

# Post process
print("Longest common suffix:", longest_Common_Suffix(strings))
