# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def rank_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0 or len(m[0]) == 0:
        return 0
    mat = [[float(val) for val in row] for row in m]
    rows_count = len(mat)
    cols_count = len(mat[0])
    rank = 0
    row = 0
    for col in range(cols_count):
        if row >= rows_count:
            break
        pivot = row
        for i in range(row + 1, rows_count):
            if abs(mat[i][col]) > abs(mat[pivot][col]):
                pivot = i
        if abs(mat[pivot][col]) <= tolerance:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        pivot_val = mat[row][col]
        for i in range(row + 1, rows_count):
            factor = mat[i][col] / pivot_val
            for j in range(col, cols_count):
                mat[i][j] -= factor * mat[row][j]
        row += 1
        rank += 1
    return rank

# Post process
print("Rank of matrix:", rank_Matrix(m))
