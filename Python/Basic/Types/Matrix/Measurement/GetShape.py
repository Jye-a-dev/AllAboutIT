# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def get_Matrix_Shape(m):
    if not m:
        return (0, 0)
    return (len(m), len(m[0]) if len(m) > 0 else 0)

# Post process
print("Matrix shape (rows, cols):", get_Matrix_Shape(m))
