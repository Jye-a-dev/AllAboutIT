# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def rotate_90_Counter_Clockwise(m):
    if not m or len(m) == 0:
        return []
    rows_count = len(m)
    cols_count = len(m[0])
    return [[m[row][col] for row in range(rows_count)] for col in range(cols_count - 1, -1, -1)]

# Post process
print("Rotated 90 degrees counter-clockwise:", rotate_90_Counter_Clockwise(m))
