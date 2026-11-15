# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Positive(a):
    return a > 0

# Post process
if is_Positive(a):
    print("The number is positive:", a)
else:
    print("The number is not positive:", a)

print("The result of is_Positive(a) is:", is_Positive(a))
