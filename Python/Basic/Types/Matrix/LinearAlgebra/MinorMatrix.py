# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
row = int(input("Enter row index to remove: "))
col = int(input("Enter column index to remove: "))

# Process
def minor_Matrix(m, row, col):
    if not m or len(m) <= 1 or len(m[0]) <= 1:
        raise ValueError("Matrix must be at least 2x2 to compute minor")
    if not (0 <= row < len(m)) or not (0 <= col < len(m[0])):
        raise IndexError("Row or column index out of bounds")
    return [[m[i][j] for j in range(len(m[0])) if j != col] for i in range(len(m)) if i != row]

# Post process
try:
    print("Submatrix after removing row and column:", minor_Matrix(m, row, col))
except Exception as e:
    print("Cannot compute minor matrix:", e)
