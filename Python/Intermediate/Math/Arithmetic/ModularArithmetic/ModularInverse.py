# Previous input
a = int(input("Enter integer a: "))
m = int(input("Enter modulus m: "))

# Process
def modular_Inverse(a, m):
    if m <= 1:
        return None
    t0, t1 = 0, 1
    r0, r1 = m, a % m
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if r0 != 1:
        return None
    return t0 % m

# Post process
print("Modular inverse of a modulo m:", modular_Inverse(a, m))
