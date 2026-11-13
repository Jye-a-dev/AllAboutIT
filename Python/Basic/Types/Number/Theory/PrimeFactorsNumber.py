# Previous input
a = int(input("Enter the number to calculate Prime prime factors for: "))
# Process
def Prime_Factor_Number(a):
    if a <= 0:
        return 0

    prime_factors = []
    d = 2
    while d * d <= a:
        while a % d == 0:
            prime_factors.append(d)
            a //= d
        d += 1
    if a > 1:
        prime_factors.append(a)
    return prime_factors
# Post process
print("The prime factors of the entered number are:", Prime_Factor_Number(a))