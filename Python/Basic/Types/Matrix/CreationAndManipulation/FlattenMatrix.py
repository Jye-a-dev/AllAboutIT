# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def flatten_Matrix(m):
    return [val for row in m for val in row]

# Post process
print("Flattened 1D array:", flatten_Matrix(m))
