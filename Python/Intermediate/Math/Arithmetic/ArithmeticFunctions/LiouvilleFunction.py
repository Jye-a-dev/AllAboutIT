# Previous input
n = int(input("Enter positive integer n: "))

# Process
def liouville_Function(n):
    if n <= 0:
        return 0
    omega = 0
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            omega += 1
            temp //= d
        d += 1
    if temp > 1:
        omega += 1
    return -1 if omega % 2 == 1 else 1

# Post process
print("Liouville function lambda(n):", liouville_Function(n))
