# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Composite(a):
    if a < 4:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return True
    return False

# Post process
if is_Composite(a):
    print("The number is a composite number:", a)
else:
    print("The number is not a composite number:", a)

print("The result of is_Composite(a) is:", is_Composite(a))
