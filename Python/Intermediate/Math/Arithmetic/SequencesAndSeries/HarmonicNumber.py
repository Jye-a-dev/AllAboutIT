# Previous input
n = int(input("Enter positive integer n: "))

# Process
def harmonic_Number(n):
    if n <= 0:
        return 0.0
    return sum(1.0 / i for i in range(1, n + 1))

# Post process
print("Harmonic number H_n:", harmonic_Number(n))
