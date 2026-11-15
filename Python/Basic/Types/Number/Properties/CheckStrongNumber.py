# Previous input
import math
a = int(input("Enter the number to check: "))

# Process
def is_Strong_Number(a):
    if a <= 0:
        return False
    return sum(math.factorial(int(d)) for d in str(a)) == a

# Post process
if is_Strong_Number(a):
    print("The number is a strong number:", a)
else:
    print("The number is not a strong number:", a)

print("The result of is_Strong_Number(a) is:", is_Strong_Number(a))
