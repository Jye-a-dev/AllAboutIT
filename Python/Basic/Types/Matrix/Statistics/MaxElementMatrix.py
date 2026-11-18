# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def max_Element_Matrix(m):
    if not m or len(m) == 0 or len(m[0]) == 0:
        raise ValueError("Cannot find maximum in empty matrix")
    return max(val for row in m for val in row)

# Post process
try:
    print("Maximum element in matrix:", max_Element_Matrix(m))
except Exception as e:
    print("Cannot find maximum element:", e)
