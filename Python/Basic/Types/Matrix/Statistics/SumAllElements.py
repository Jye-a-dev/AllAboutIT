# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def sum_All_Elements(m):
    return sum(val for row in m for val in row) if m else 0

# Post process
print("Sum of all elements in matrix:", sum_All_Elements(m))
