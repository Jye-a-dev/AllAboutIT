# Previous input
strings = input("Enter strings separated by comma: ").split(",")

# Process
def longest_Common_Prefix(strings):
    if not strings:
        return ""
    prefix = strings[0].strip()
    for s in strings[1:]:
        s = s.strip()
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Post process
print("Longest common prefix:", longest_Common_Prefix(strings))
