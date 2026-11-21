# Previous input
n = int(input("Enter positive integer n: "))

# Process
def mobius_Function(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    p_count = 0
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            p_count += 1
            temp //= d
            if temp % d == 0:
                return 0
        d += 1
    if temp > 1:
        p_count += 1
    return -1 if p_count % 2 == 1 else 1

# Post process
print("Mobius function mu(n):", mobius_Function(n))
