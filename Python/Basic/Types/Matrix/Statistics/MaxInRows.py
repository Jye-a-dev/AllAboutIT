# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def max_In_Rows(m):
    if not m:
        return []
    return [max(row) for row in m]

# Post process
try:
    print("Maximum elements in each row:", max_In_Rows(m))
except Exception as e:
    print("Cannot find maximum in rows:", e)
