# Previous input
a = input("Enter the first string: ")
b = input("Enter the second string: ")

# Process
def is_Anagram(a, b):
    clean_a = [c.lower() for c in a if not c.isspace()]
    clean_b = [c.lower() for c in b if not c.isspace()]
    return sorted(clean_a) == sorted(clean_b)

# Post process
print("Are anagrams:", is_Anagram(a, b))
