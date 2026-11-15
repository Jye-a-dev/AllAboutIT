# Previous input
n = float(input("Enter the number to check: "))

# Process
def is_Zero(n):
    return n == 0

# Post process
if is_Zero(n):
    print("The number is zero:", n)
else:
    print("The number is not zero:", n)

print("The result of is_Zero(n) is:", is_Zero(n))
