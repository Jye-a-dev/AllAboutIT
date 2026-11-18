# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def flip_Horizontal(m):
    return [row[::-1] for row in m]

# Post process
print("Horizontally flipped matrix:", flip_Horizontal(m))
