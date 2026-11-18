# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def count_Rows(m):
    return len(m) if m else 0

# Post process
print("Number of rows:", count_Rows(m))
