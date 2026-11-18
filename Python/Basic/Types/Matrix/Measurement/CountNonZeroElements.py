# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def count_Non_Zero_Elements(m, tolerance=1e-9):
    if not m:
        return 0
    return sum(1 for row in m for val in row if abs(val) > tolerance)

# Post process
print("Count of non-zero elements:", count_Non_Zero_Elements(m))
