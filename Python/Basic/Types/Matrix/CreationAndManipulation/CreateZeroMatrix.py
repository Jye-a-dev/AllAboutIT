# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Process
def create_Zero_Matrix(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("Dimensions must be non-negative")
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Post process
try:
    print("Zero matrix:", create_Zero_Matrix(rows, cols))
except Exception as e:
    print("Cannot create zero matrix:", e)
