# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Square_Matrix(m):
    if not m or len(m) == 0:
        return False
    rows_count = len(m)
    return all(len(row) == rows_count for row in m)

# Post process
print("Is square matrix:", is_Square_Matrix(m))
