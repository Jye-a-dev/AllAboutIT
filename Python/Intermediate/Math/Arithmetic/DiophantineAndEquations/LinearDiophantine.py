import math

# Previous input
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter constant c: "))

# Process
def solve_Linear_Diophantine(a, b, c):
    if a == 0 and b == 0:
        return (0, 0) if c == 0 else None
    if a == 0:
        return (0, c // b) if c % b == 0 else None
    if b == 0:
        return (c // a, 0) if c % a == 0 else None

    # Extended GCD
    x0, x1, y0, y1 = 1, 0, 0, 1
    curr_a, curr_b = a, b
    while curr_b != 0:
        q = curr_a // curr_b
        curr_a, curr_b = curr_b, curr_a % curr_b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    gcd = curr_a
    if gcd < 0:
        gcd, x0, y0 = -gcd, -x0, -y0

    if c % gcd != 0:
        return None
    scale = c // gcd
    return (x0 * scale, y0 * scale)

# Post process
print("Particular solution (x, y):", solve_Linear_Diophantine(a, b, c))
