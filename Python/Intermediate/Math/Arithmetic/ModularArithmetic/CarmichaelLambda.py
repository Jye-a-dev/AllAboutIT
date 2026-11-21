import math

# Previous input
n = int(input("Enter positive integer n: "))

# Process
def carmichael_Lambda(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    def prime_factors(num):
        factors = {}
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors[d] = factors.get(d, 0) + 1
                num //= d
            d += 1
        if num > 1:
            factors[num] = factors.get(num, 0) + 1
        return factors

    def lambda_prime_power(p, k):
        if p == 2:
            if k == 1:
                return 1
            if k == 2:
                return 2
            return 2 ** (k - 2)
        return (p ** (k - 1)) * (p - 1)

    factors = prime_factors(n)
    lcm_val = 1
    for p, k in factors.items():
        val = lambda_prime_power(p, k)
        lcm_val = (lcm_val * val) // math.gcd(lcm_val, val)
    return lcm_val

# Post process
print("Carmichael lambda(n):", carmichael_Lambda(n))
