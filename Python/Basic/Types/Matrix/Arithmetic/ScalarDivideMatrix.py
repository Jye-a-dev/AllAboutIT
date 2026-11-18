# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
k = float(input("Enter scalar divisor: "))

# Process
def scalar_Divide_Matrix(m, k):
    if k == 0:
        raise ZeroDivisionError("Cannot divide matrix by zero")
    return [[val / k for val in row] for row in m]

# Post process
try:
    print("Matrix after scalar division:", scalar_Divide_Matrix(m, k))
except Exception as e:
    print("Cannot divide matrix by scalar:", e)
