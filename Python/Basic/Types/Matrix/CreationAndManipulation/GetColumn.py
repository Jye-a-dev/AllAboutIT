# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
col_idx = int(input("Enter column index to extract: "))

# Process
def get_Column(m, col_idx):
    if not m or not (0 <= col_idx < len(m[0])):
        raise IndexError("Column index out of range")
    return [row[col_idx] for row in m]

# Post process
try:
    print("Extracted column:", get_Column(m, col_idx))
except Exception as e:
    print("Cannot extract column:", e)
