# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def min_In_Rows(m):
    if not m:
        return []
    return [min(row) for row in m]

# Post process
try:
    print("Minimum elements in each row:", min_In_Rows(m))
except Exception as e:
    print("Cannot find minimum in rows:", e)
