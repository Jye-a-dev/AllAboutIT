# Previous input
n1 = int(input("Enter number: "))

# Process
def Cube_Root_Number(n, b=None):
    val = n * b if b is not None else n
    if val < 0:
        return -(abs(val) ** (1 / 3))
    return val ** (1 / 3)

# Post process
print("The cube root of the entered number is:", Cube_Root_Number(n1))
