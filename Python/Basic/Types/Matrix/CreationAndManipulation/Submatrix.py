# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
start_row = int(input("Enter start row: "))
end_row = int(input("Enter end row (exclusive): "))
start_col = int(input("Enter start col: "))
end_col = int(input("Enter end col (exclusive): "))

# Process
def extract_Submatrix(m, start_row, end_row, start_col, end_col):
    if not m:
        return []
    return [[m[i][j] for j in range(start_col, min(end_col, len(m[0])))] for i in range(start_row, min(end_row, len(m)))]

# Post process
print("Extracted submatrix:", extract_Submatrix(m, start_row, end_row, start_col, end_col))
