# Previous input
n = int(input("Enter positive integer n: "))

# Process
def euler_Totient(n):
    if n <= 0:
        return 0
    res = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            res -= res // p
        p += 1
    if temp > 1:
        res -= res // temp
    return res

# Post process
print("Euler's totient phi(n):", euler_Totient(n))
