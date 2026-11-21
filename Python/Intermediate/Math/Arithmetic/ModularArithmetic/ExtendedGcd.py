# Previous input
a = int(input("Enter first integer a: "))
b = int(input("Enter second integer b: "))

# Process
def extended_Gcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    x0, x1, y0, y1 = 1, 0, 0, 1
    orig_a, orig_b = a, b
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if a < 0:
        a, x0, y0 = -a, -x0, -y0
    return (a, x0, y0)

# Post process
print("Extended GCD result (gcd, x, y):", extended_Gcd(a, b))
