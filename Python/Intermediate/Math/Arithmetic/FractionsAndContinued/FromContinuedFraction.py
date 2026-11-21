import math

# Previous input
coefficients = [int(x.strip()) for x in input("Enter continued fraction coefficients (comma-separated): ").split(",") if x.strip()]

# Process
def from_Continued_Fraction(coefficients):
    if not coefficients:
        return (0, 1)
    num = coefficients[-1]
    den = 1
    for a in reversed(coefficients[:-1]):
        num, den = a * num + den, num
    g = math.gcd(num, den)
    num //= g
    den //= g
    if den < 0:
        num, den = -num, -den
    return (num, den)

# Post process
print("Fraction from continued fraction (num, den):", from_Continued_Fraction(coefficients))
