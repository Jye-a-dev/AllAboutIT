# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def min_In_Columns(m):
    if not m or len(m) == 0:
        return []
    return [min(m[i][j] for i in range(len(m))) for j in range(len(m[0]))]

# Post process
try:
    print("Minimum elements in each column:", min_In_Columns(m))
except Exception as e:
    print("Cannot find minimum in columns:", e)
