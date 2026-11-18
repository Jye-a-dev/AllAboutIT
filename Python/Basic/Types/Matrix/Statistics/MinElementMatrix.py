# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def min_Element_Matrix(m):
    if not m or len(m) == 0 or len(m[0]) == 0:
        raise ValueError("Cannot find minimum in empty matrix")
    return min(val for row in m for val in row)

# Post process
try:
    print("Minimum element in matrix:", min_Element_Matrix(m))
except Exception as e:
    print("Cannot find minimum element:", e)
