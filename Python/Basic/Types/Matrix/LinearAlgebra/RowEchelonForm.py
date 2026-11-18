# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def to_Row_Echelon_Form(m, tolerance=1e-9):
    if not m or len(m) == 0:
        return []
    mat = [[float(val) for val in row] for row in m]
    rows_count = len(mat)
    cols_count = len(mat[0])
    lead = 0
    for r in range(rows_count):
        if lead >= cols_count:
            break
        i = r
        while abs(mat[i][lead]) <= tolerance:
            i += 1
            if i == rows_count:
                i = r
                lead += 1
                if lead == cols_count:
                    return mat
        mat[i], mat[r] = mat[r], mat[i]
        pivot = mat[r][lead]
        if abs(pivot) > tolerance:
            mat[r] = [val / pivot for val in mat[r]]
        for i in range(r + 1, rows_count):
            factor = mat[i][lead]
            mat[i] = [val - factor * base for val, base in zip(mat[i], mat[r])]
        lead += 1
    return mat

# Post process
print("Row Echelon Form (REF):", to_Row_Echelon_Form(m))
