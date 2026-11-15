# Previous input
n = float(input("Enter the number to check: "))

# Process
def is_Negative(n):
    return n < 0

# Post process
if is_Negative(n):
    print("The number is negative:", n)
else:
    print("The number is not negative:", n)

print("The result of is_Negative(n) is:", is_Negative(n))
