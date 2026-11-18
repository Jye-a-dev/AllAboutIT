# Previous input
n = int(input("Enter matrix dimension n: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Process
def inverse_NxN(m, tolerance=1e-12):
    if not m or any(len(row) != len(m) for row in m):
        raise ValueError("Inverse requires a non-empty square matrix")
    n = len(m)
    aug = [[float(m[i][j]) for j in range(n)] + [1.0 if i == k else 0.0 for k in range(n)] for i in range(n)]
    for col in range(n):
        pivot = col
        for row in range(col + 1, n):
            if abs(aug[row][col]) > abs(aug[pivot][col]):
                pivot = row
        if abs(aug[pivot][col]) <= tolerance:
            raise ValueError("Matrix is singular and cannot be inverted")
        if pivot != col:
            aug[pivot], aug[col] = aug[col], aug[pivot]
        pivot_val = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= pivot_val
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                for j in range(col, 2 * n):
                    aug[row][j] -= factor * aug[col][j]
    return [[aug[i][j + n] for j in range(n)] for i in range(n)]

# Post process
try:
    print("Inverse of NxN matrix:", inverse_NxN(m))
except Exception as e:
    print("Cannot invert NxN matrix:", e)
