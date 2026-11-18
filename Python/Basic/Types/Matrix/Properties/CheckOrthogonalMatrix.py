# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Orthogonal_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0:
        return False
    n = len(m)
    if any(len(row) != n for row in m):
        return False
    for i in range(n):
        for j in range(n):
            dot = sum(m[i][k] * m[j][k] for k in range(n))
            expected = 1.0 if i == j else 0.0
            if abs(dot - expected) > tolerance:
                return False
    return True

# Post process
print("Is orthogonal matrix:", is_Orthogonal_Matrix(m))
