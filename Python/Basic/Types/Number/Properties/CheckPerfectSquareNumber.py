# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Perfect_Square(a):
    if a < 0:
        return False
    sqrt_a = int(a ** 0.5)
    return sqrt_a * sqrt_a == a

# Post process
if is_Perfect_Square(a):
    print("The number is a perfect square:", a)
else:
    print("The number is not a perfect square:", a)

print("The result of is_Perfect_Square(a) is:", is_Perfect_Square(a))
