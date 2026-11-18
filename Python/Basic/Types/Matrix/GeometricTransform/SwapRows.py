# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
row1 = int(input("Enter first row index: "))
row2 = int(input("Enter second row index: "))

# Process
def swap_Rows(m, row1, row2):
    if not (0 <= row1 < len(m)) or not (0 <= row2 < len(m)):
        raise IndexError("Row index out of range")
    res = [list(r) for r in m]
    res[row1], res[row2] = res[row2], res[row1]
    return res

# Post process
try:
    print("Matrix after swapping rows:", swap_Rows(m, row1, row2))
except Exception as e:
    print("Cannot swap rows:", e)
