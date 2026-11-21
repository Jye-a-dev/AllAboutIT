import math

# Previous input
n = int(input("Enter modulus n: "))

# Process
def find_Primitive_Root(n):
    if n <= 1:
        return None
    if n == 2:
        return 1
    if n == 4:
        return 3

    # Euler totient
    phi = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            phi -= phi // p
        p += 1
    if temp > 1:
        phi -= phi // temp

    # Prime factors of phi
    phi_factors = set()
    temp = phi
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            phi_factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        phi_factors.add(temp)

    for g in range(2, n):
        if math.gcd(g, n) == 1:
            is_primitive = True
            for factor in phi_factors:
                if pow(g, phi // factor, n) == 1:
                    is_primitive = False
                    break
            if is_primitive:
                return g
    return None

# Post process
print("Smallest primitive root modulo n:", find_Primitive_Root(n))
