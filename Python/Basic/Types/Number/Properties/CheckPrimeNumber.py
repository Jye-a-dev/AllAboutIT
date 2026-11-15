# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

# Post process
if is_Prime(a):
    print("The number is prime:", a)
else:
    print("The number is not prime:", a)

print("The result of is_Prime(a) is:", is_Prime(a))
