# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def sum_Rows(m):
    return [sum(row) for row in m]

# Post process
print("Sum of elements in each row:", sum_Rows(m))
