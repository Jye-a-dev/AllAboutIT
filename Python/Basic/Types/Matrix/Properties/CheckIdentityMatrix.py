# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Identity_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0:
        return False
    n = len(m)
    for i in range(n):
        if len(m[i]) != n:
            return False
        for j in range(n):
            expected = 1.0 if i == j else 0.0
            if abs(m[i][j] - expected) > tolerance:
                return False
    return True

# Post process
print("Is identity matrix:", is_Identity_Matrix(m))
