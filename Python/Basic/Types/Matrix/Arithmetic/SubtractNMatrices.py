# Previous input
n = int(input("Enter number of matrices: "))
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrices = []
for idx in range(n):
    print(f"Matrix {idx + 1}:")
    mat = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
    matrices.append(mat)

# Process
def subtract_N_Matrices(matrices):
    if not matrices:
        return []
    res = [[val for val in row] for row in matrices[0]]
    rows_count, cols_count = len(res), len(res[0])
    for m in matrices[1:]:
        if len(m) != rows_count or any(len(r) != cols_count for r in m):
            raise ValueError("All matrices must have identical dimensions")
        for i in range(rows_count):
            for j in range(cols_count):
                res[i][j] -= m[i][j]
    return res

# Post process
try:
    print("Result of subtracting N matrices:", subtract_N_Matrices(matrices))
except Exception as e:
    print("Cannot subtract N matrices:", e)
