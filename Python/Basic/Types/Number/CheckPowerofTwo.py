# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_power_of_two(a):
    if a < 1:
        return False
    while a % 2 == 0:
        a //= 2
    return a == 1

# Post process
if is_power_of_two(a):
    print("The number is a power of two:", a)
else:
    print("The number is not a power of two:", a)

print("The result of is_power_of_two(a) is:", is_power_of_two(a)) 
