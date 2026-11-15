# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Automorphic(a):
    if a < 0:
        return False
    square = a * a
    return str(square).endswith(str(a))

# Post process
if is_Automorphic(a):
    print("The number is an automorphic number:", a)
else:
    print("The number is not an automorphic number:", a)

print("The result of is_Automorphic(a) is:", is_Automorphic(a))
