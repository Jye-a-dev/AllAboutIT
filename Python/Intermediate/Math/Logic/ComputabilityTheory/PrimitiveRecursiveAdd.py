# Previous input
x = int(input("Enter non-negative integer x: "))
y = int(input("Enter non-negative integer y: "))

# Process
def primitive_Recursive_Add(x, y):
    if x < 0 or y < 0:
        raise ValueError("Inputs must be non-negative integers")
    res = x
    for _ in range(y):
        res += 1  # Successor operation S(res)
    return res

# Post process
print("Primitive recursive sum:", primitive_Recursive_Add(x, y))
