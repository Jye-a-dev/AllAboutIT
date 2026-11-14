# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_positive(a):
    return a > 0

# Post process
if is_positive(a):
    print("The number is positive:", a)
else:
    print("The number is not positive:", a)

print("The result of is_positive(a) is:", is_positive(a)) 
