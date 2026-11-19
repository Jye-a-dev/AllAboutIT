# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def is_Palindrome_List(a):
    return a == a[::-1]

# Post process
print("The list is a palindrome:", is_Palindrome_List(a))
