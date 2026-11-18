# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Empty_Matrix(m):
    return not m or len(m) == 0 or all(len(row) == 0 for row in m)

# Post process
print("Is empty matrix:", is_Empty_Matrix(m))
