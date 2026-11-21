# Previous input
a = int(input("Enter integer a: "))
p = int(input("Enter odd prime p: "))

# Process
def legendre_Symbol(a, p):
    if p <= 2:
        raise ValueError("Modulus p must be an odd prime")
    a = a % p
    if a == 0:
        return 0
    res = pow(a, (p - 1) // 2, p)
    return -1 if res == p - 1 else res

# Post process
print("Legendre symbol (a/p):", legendre_Symbol(a, p))
