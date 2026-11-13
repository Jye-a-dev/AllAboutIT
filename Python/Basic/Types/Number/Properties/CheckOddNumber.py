# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_odd(a):
    return a % 2 == 1

# Post process
if is_odd(a):
    print("The number is odd:", a)
else:
    print("The number is not odd:", a)

print("The result of is_odd(a) is:", is_odd(a)) 