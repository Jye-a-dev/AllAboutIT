# Previous input
n = int(input("Enter the number of strings to add: "))
# Process
def plus_strings(n):
    strings = []
    for i in range(n):
        s = input(f"Enter string {i + 1}: ")
        strings.append(s)
    return ''.join(strings)
# Post process
print("The combined string is:", plus_strings(n))