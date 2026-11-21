# Previous input
x = int(input("Enter integer limit x: "))

# Process
def prime_Counting_Pi(x):
    if x < 2:
        return 0
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= x:
        if sieve[p]:
            for i in range(p * p, x + 1, p):
                sieve[i] = False
        p += 1
    return sum(sieve)

# Post process
print("Prime counting function pi(x):", prime_Counting_Pi(x))
