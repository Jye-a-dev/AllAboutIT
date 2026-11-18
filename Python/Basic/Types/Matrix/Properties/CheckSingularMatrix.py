# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Singular_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0:
        return False
    n = len(m)
    if any(len(row) != n for row in m):
        return False
    mat = [[float(val) for val in row] for row in m]
    det = 1.0
    for col in range(n):
        pivot = col
        for row in range(col + 1, n):
            if abs(mat[row][col]) > abs(mat[pivot][col]):
                pivot = row
        if abs(mat[pivot][col]) <= tolerance:
            return True
        if pivot != col:
            mat[pivot], mat[col] = mat[col], mat[pivot]
            det = -det
        det *= mat[col][col]
        pivot_val = mat[col][col]
        for row in range(col + 1, n):
            factor = mat[row][col] / pivot_val
            for k in range(col + 1, n):
                mat[row][k] -= factor * mat[col][k]
    return abs(det) <= tolerance

# Post process
print("Is singular matrix:", is_Singular_Matrix(m))
