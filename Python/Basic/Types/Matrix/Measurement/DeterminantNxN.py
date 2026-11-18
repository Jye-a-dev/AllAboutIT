# Previous input
n = int(input("Enter matrix dimension n: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Process
def determinant_NxN(m):
    if not m or any(len(row) != len(m) for row in m):
        raise ValueError("Matrix must be non-empty and square")
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    mat = [[float(val) for val in row] for row in m]
    det = 1.0
    for col in range(n):
        pivot = col
        for row in range(col + 1, n):
            if abs(mat[row][col]) > abs(mat[pivot][col]):
                pivot = row
        if abs(mat[pivot][col]) < 1e-12:
            return 0.0
        if pivot != col:
            mat[pivot], mat[col] = mat[col], mat[pivot]
            det = -det
        det *= mat[col][col]
        pivot_val = mat[col][col]
        for row in range(col + 1, n):
            factor = mat[row][col] / pivot_val
            for k in range(col + 1, n):
                mat[row][k] -= factor * mat[col][k]
    return det

# Post process
try:
    print("Determinant of NxN matrix:", determinant_NxN(m))
except Exception as e:
    print("Cannot compute NxN determinant:", e)
