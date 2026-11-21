# Previous input
m = int(input("Enter non-negative integer m: "))
n = int(input("Enter non-negative integer n: "))

# Process
def ackermann_Function(m, n):
    if m < 0 or n < 0:
        raise ValueError("Arguments must be non-negative integers")
    stack = [m]
    while stack:
        curr_m = stack.pop()
        if curr_m == 0:
            n = n + 1
        elif n == 0:
            stack.append(curr_m - 1)
            n = 1
        else:
            stack.append(curr_m - 1)
            stack.append(curr_m)
            n = n - 1
    return n

# Post process
print("Ackermann value A(m, n):", ackermann_Function(m, n))
