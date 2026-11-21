import math

# Previous input
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

# Process
def simplify_Fraction(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    g = math.gcd(numerator, denominator)
    num = numerator // g
    den = denominator // g
    if den < 0:
        num, den = -num, -den
    return (num, den)

# Post process
print("Simplified fraction (num, den):", simplify_Fraction(numerator, denominator))
