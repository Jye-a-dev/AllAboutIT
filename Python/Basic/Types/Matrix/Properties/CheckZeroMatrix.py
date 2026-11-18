# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Zero_Matrix(m, tolerance=1e-9):
    if not m or len(m) == 0 or len(m[0]) == 0:
        return False
    return all(abs(val) <= tolerance for row in m for val in row)

# Post process
print("Is zero matrix:", is_Zero_Matrix(m))
