# Previous input
n = int(input("Enter positive integer n: "))
k = int(input("Enter power k (default 1): "))

# Process
def sum_Divisors_Sigma(n, k=1):
    if n <= 0:
        return 0
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d ** k
            if d * d != n:
                total += (n // d) ** k
        d += 1
    return total

# Post process
print("Sum of divisors sigma_k(n):", sum_Divisors_Sigma(n, k))
