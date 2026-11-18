# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def count_Columns(m):
    return len(m[0]) if m and len(m) > 0 else 0

# Post process
print("Number of columns:", count_Columns(m))
