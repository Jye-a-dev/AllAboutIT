# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def get_Anti_Diagonal(m):
    if not m:
        return []
    rows_count, cols_count = len(m), len(m[0])
    limit = min(rows_count, cols_count)
    return [m[i][cols_count - 1 - i] for i in range(limit)]

# Post process
print("Anti-diagonal elements:", get_Anti_Diagonal(m))
