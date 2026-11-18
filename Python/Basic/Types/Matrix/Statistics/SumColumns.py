# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def sum_Columns(m):
    if not m or len(m) == 0:
        return []
    return [sum(m[i][j] for i in range(len(m))) for j in range(len(m[0]))]

# Post process
print("Sum of elements in each column:", sum_Columns(m))
