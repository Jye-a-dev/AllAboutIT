# Previous input
n = int(input("Enter the number to check: "))

# Process
def is_Even(n):
    return n % 2 == 0

# Post process
if is_Even(n):
    print("The number is even:", n)
else:
    print("The number is not even:", n)

print("The result of is_Even(n) is:", is_Even(n))
