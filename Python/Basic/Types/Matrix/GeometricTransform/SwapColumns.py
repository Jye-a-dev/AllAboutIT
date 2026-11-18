# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
col1 = int(input("Enter first column index: "))
col2 = int(input("Enter second column index: "))

# Process
def swap_Columns(m, col1, col2):
    if not m or not (0 <= col1 < len(m[0])) or not (0 <= col2 < len(m[0])):
        raise IndexError("Column index out of range")
    res = []
    for r in m:
        row = list(r)
        row[col1], row[col2] = row[col2], row[col1]
        res.append(row)
    return res

# Post process
try:
    print("Matrix after swapping columns:", swap_Columns(m, col1, col2))
except Exception as e:
    print("Cannot swap columns:", e)
