# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def negate_Matrix(m):
    return [[-val for val in row] for row in m]

# Post process
print("Negated matrix:", negate_Matrix(m))
