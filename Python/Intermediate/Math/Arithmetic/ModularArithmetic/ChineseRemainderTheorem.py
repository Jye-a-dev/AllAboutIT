import math

# Previous input
remainders = [int(x.strip()) for x in input("Enter remainders (comma-separated): ").split(",") if x.strip()]
moduli = [int(x.strip()) for x in input("Enter moduli (comma-separated): ").split(",") if x.strip()]

# Process
def solve_Chinese_Remainder(remainders, moduli):
    if len(remainders) != len(moduli) or len(moduli) == 0:
        return None
    # Check pairwise coprimality
    for i in range(len(moduli)):
        if moduli[i] <= 0:
            return None
        for j in range(i + 1, len(moduli)):
            if math.gcd(moduli[i], moduli[j]) != 1:
                return None
    total_m = 1
    for m in moduli:
        total_m *= m
    x = 0
    for r, m in zip(remainders, moduli):
        m_i = total_m // m
        # compute inverse of m_i modulo m
        t0, t1 = 0, 1
        r0, r1 = m, m_i % m
        while r1 != 0:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1
            t0, t1 = t1, t0 - q * t1
        inv = t0 % m
        x = (x + r * m_i * inv) % total_m
    return x

# Post process
print("Solution by Chinese Remainder Theorem:", solve_Chinese_Remainder(remainders, moduli))
