# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Palindrome(a):
    # Convert the number to a string
    str_a = str(a)
    # Check if the string is equal to its reverse
    return str_a == str_a[::-1]

# Post process
if is_Palindrome(a):
    print("The number is a palindrome:", a)
else:
    print("The number is not a palindrome:", a)

print("The result of is_Palindrome(a) is:", is_Palindrome(a))
