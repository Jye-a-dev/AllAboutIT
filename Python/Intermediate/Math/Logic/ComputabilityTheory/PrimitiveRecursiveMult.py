# Previous input
x = int(input("Enter non-negative integer x: "))
y = int(input("Enter non-negative integer y: "))

# Process
def primitive_Recursive_Mult(x, y):
    if x < 0 or y < 0:
        raise ValueError("Inputs must be non-negative integers")
    res = 0
    for _ in range(y):
        # Addition step
        for _ in range(x):
            res += 1
    return res

# Post process
print("Primitive recursive product:", primitive_Recursive_Mult(x, y))
