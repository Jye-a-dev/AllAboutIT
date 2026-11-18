# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Scalar_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0:
        return False
    n = len(m)
    if any(len(row) != n for row in m):
        return False
    scalar_val = m[0][0]
    for i in range(n):
        for j in range(n):
            if i == j:
                if abs(m[i][j] - scalar_val) > tolerance:
                    return False
            else:
                if abs(m[i][j]) > tolerance:
                    return False
    return True

# Post process
print("Is scalar matrix:", is_Scalar_Matrix(m))
