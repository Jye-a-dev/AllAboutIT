import math

# Previous input
f1 = [int(x.strip()) for x in input("Enter fraction 1 (num, den): ").split(",") if x.strip()]
f2 = [int(x.strip()) for x in input("Enter fraction 2 (num, den): ").split(",") if x.strip()]

# Process
def add_Fractions(f1, f2):
    n1, d1 = f1[0], f1[1]
    n2, d2 = f2[0], f2[1]
    if d1 == 0 or d2 == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    g = math.gcd(num, den)
    num //= g
    den //= g
    if den < 0:
        num, den = -num, -den
    return (num, den)

# Post process
print("Sum of fractions:", add_Fractions(f1, f2))
