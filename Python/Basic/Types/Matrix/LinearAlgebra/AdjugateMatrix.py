# Previous input
n = int(input("Enter matrix dimension n: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Process
def _det_helper(mat):
    k = len(mat)
    if k == 1:
        return mat[0][0]
    if k == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    temp = [[float(v) for v in row] for row in mat]
    det_val = 1.0
    for col in range(k):
        pivot = col
        for row in range(col + 1, k):
            if abs(temp[row][col]) > abs(temp[pivot][col]):
                pivot = row
        if abs(temp[pivot][col]) < 1e-12:
            return 0.0
        if pivot != col:
            temp[pivot], temp[col] = temp[col], temp[pivot]
            det_val = -det_val
        det_val *= temp[col][col]
        pv = temp[col][col]
        for row in range(col + 1, k):
            factor = temp[row][col] / pv
            for j in range(col + 1, k):
                temp[row][j] -= factor * temp[col][j]
    return det_val

def adjugate_Matrix(m):
    if not m or any(len(row) != len(m) for row in m):
        raise ValueError("Adjugate matrix requires a non-empty square matrix")
    n = len(m)
    if n == 1:
        return [[1]]
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[m[r][c] for c in range(n) if c != j] for r in range(n) if r != i]
            sign = 1 if (i + j) % 2 == 0 else -1
            adj[j][i] = sign * _det_helper(minor)
    return adj

# Post process
try:
    print("Adjugate matrix:", adjugate_Matrix(m))
except Exception as e:
    print("Cannot compute adjugate matrix:", e)
