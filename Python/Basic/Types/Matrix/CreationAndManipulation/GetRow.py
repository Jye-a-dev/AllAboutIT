# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
row_idx = int(input("Enter row index to extract: "))

# Process
def get_Row(m, row_idx):
    if not (0 <= row_idx < len(m)):
        raise IndexError("Row index out of range")
    return list(m[row_idx])

# Post process
try:
    print("Extracted row:", get_Row(m, row_idx))
except Exception as e:
    print("Cannot extract row:", e)
