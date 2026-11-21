# Previous input
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

# Process
def to_Continued_Fraction(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    res = []
    a, b = numerator, denominator
    while b != 0:
        q = a // b
        res.append(q)
        a, b = b, a - q * b
    return res

# Post process
print("Continued fraction representation:", to_Continued_Fraction(numerator, denominator))
