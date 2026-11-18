# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def count_Total_Elements(m):
    return sum(len(row) for row in m) if m else 0

# Post process
print("Total number of elements:", count_Total_Elements(m))
