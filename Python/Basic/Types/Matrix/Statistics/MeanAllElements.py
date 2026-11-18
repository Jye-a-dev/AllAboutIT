# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def mean_All_Elements(m):
    if not m or len(m) == 0:
        raise ValueError("Cannot calculate mean of empty matrix")
    total = sum(val for row in m for val in row)
    count = sum(len(row) for row in m)
    if count == 0:
        raise ValueError("Matrix contains zero elements")
    return total / count

# Post process
try:
    print("Mean of all elements in matrix:", mean_All_Elements(m))
except Exception as e:
    print("Cannot calculate mean:", e)
