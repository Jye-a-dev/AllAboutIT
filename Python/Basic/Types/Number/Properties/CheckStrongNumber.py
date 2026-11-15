# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Strong_Number(a):
    if a < 4:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return True
    return False

# Post process
if is_Strong_Number(a):
    print("The number is a strong number:", a)
else:
    print("The number is not a strong number:", a)

print("The result of is_Strong_Number(a) is:", is_Strong_Number(a))
