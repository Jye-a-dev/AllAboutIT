# Previous input
n = int(input("Enter matrix dimension n: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(n)]
p = int(input("Enter power exponent: "))

# Process
def power_Matrix(m, p):
    if not m or any(len(row) != len(m) for row in m):
        raise ValueError("Power requires a square matrix")
    if not isinstance(p, int) or p < 0:
        raise ValueError("Power must be a non-negative integer")
    n = len(m)
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [[val for val in row] for row in m]
    while p > 0:
        if p % 2 == 1:
            res = [[sum(res[i][k] * base[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        base = [[sum(base[i][k] * base[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        p //= 2
    return res

# Post process
try:
    print("Matrix raised to power:", power_Matrix(m, p))
except Exception as e:
    print("Cannot compute matrix power:", e)
