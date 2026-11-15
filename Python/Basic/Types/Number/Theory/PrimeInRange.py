# Previous input
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Process
def Prime_In_Range(a, b):
    start, end = sorted((a, b))
    if end < 2:
        return []
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(end**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, end + 1, p):
                sieve[i] = False
    return [i for i in range(max(2, start), end + 1) if sieve[i]]

# Post process
print("The prime numbers in the range are:", Prime_In_Range(n1, n2))
