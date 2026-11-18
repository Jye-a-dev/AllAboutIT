# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def max_In_Columns(m):
    if not m or len(m) == 0:
        return []
    return [max(m[i][j] for i in range(len(m))) for j in range(len(m[0]))]

# Post process
try:
    print("Maximum elements in each column:", max_In_Columns(m))
except Exception as e:
    print("Cannot find maximum in columns:", e)
