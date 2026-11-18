import math

# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def frobenius_Norm(m):
    if not m or len(m) == 0:
        return 0.0
    return math.sqrt(sum(val ** 2 for row in m for val in row))

# Post process
print("Frobenius norm of matrix:", frobenius_Norm(m))
