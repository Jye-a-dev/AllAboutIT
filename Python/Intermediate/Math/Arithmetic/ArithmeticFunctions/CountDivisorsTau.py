# Previous input
n = int(input("Enter positive integer n: "))

# Process
def count_Divisors_Tau(n):
    if n <= 0:
        return 0
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 1 if d * d == n else 2
        d += 1
    return count

# Post process
print("Number of divisors tau(n):", count_Divisors_Tau(n))
