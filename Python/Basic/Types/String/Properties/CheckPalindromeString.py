# Previous input
a = input("Enter the string: ")

# Process
def is_Palindrome(a):
    return a == a[::-1]

# Post process
print("Is palindrome:", is_Palindrome(a))
